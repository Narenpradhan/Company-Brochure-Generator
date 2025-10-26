import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from openai import OpenAI
from scraper import fetch_website_contents, fetch_website_links

load_dotenv(override=True)

class BrochureGenerator:
    def __init__(self, api_key, base_url, llm_model):
        # self.company_name = comapny_name
        # self.company_url = company_url
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.llm_model = llm_model


    # System prompt for filtering links
    link_system_prompt = """
    You are provided with a list of links found on a webpage.
    You are able to decide which of the links would be most relevant to include in a brochure about the company,
    such as links to an About page, or a Company page, or Careers/Jobs pages.
    You should respond in JSON as in this example without code block:

    {
        "links": [
            {"type": "about page", "url": "https://full.url/goes/here/about"},
            {"type": "careers page", "url": "https://another.full.url/careers"}
        ]
    }
    """


    # User prompt for filtering links
    def craft_link_user_prompt(self, url):
        user_prompt = """
        Here is the list of links on the website {url} -
        Please decide which of these are relevant web links for a brochure about the company, 
        respond with the full https URL in JSON format.
        Do not include Terms of Service, Privacy, email links.

        Links (some might be relative links):

        """
        print("Fetching website links ....")
        links = fetch_website_links(url)
        user_prompt += "\n".join(links)
        return user_prompt.format(url=url)
    

    # Function to filter relevant links using LLM
    def filter_relevant_links(self, url):
        response = self.client.chat.completions.create(
            model=self.llm_model,
            messages=[
                {"role": "system", "content":self.link_system_prompt},
                {"role":"user", "content": self.craft_link_user_prompt(url)}
            ],
            response_format={"type": "json_object"}
        )

        print("Filtering relevant links ....")
        result = response.choices[0].message.content
        links = json.loads(result)
        return links
    

    # Function to fetch contents from landing page and relevant links
    def fetch_link_contents(self, url):
        print("Fetching website contents ....")
        landing_page_content = fetch_website_contents(url)
        relevant_links = self.filter_relevant_links(url)
        result = f"## Landing Page:\n\n{landing_page_content}\n## Relevant Links:\n"
        for link in relevant_links['links']:
            result += f"\n\n### Link: {link['url']}\n"
            result += fetch_website_contents(link['url'])
        return result
    

    brochure_system_prompt = """
    You are a marketing expert tasked with creating a short brochure in markdown format for a company.
    You will be provided with the contents of the company's landing page and other relevant pages.
    Use this information to create an engaging and informative brochure that highlights the company's mission, values,  products/services, careers/jobs and any other pertinent details.
    Respond in markdown format without code blocks.
    """


    # User prompt for crafting brochure
    def craft_brochure_prompt(self, company_name, url):
        user_prompt = f"""
    You are looking at a company called: {company_name}
    Here are the contents of its landing page and other relevant pages;
    use this information to build a short brochure of the company in markdown without code blocks.\n\n
    """
        user_prompt += self.fetch_link_contents(url)
        return user_prompt
    

    # Function to create brochure using LLM
    def create_brochure(self, company_name, url):
        response = self.client.chat.completions.create(
            model=self.llm_model,
            messages=[
                {"role": "system", "content": self.brochure_system_prompt},
                {"role": "user", "content": self.craft_brochure_prompt(company_name, url)}
            ],
            # stream=True # uncomment this line to stream the brochure content
        )

        print("\nGenerating Brochure Content ....)
        brochure_content = response.choices[0].message.content
        return brochure_content

        # uncomment this line to stream the brochure content
        # brochure_content = ""
        # display_handle = display(Markdown(""), display_id=True)   only works in Jupyter Notebook     
        # for chunk in response:
        #     brochure_content += chunk.choices[0].delta.content or ""
        #     # update_display(Markdown(brochure_content), display_id=display_handle.display_id)  only works in Jupyter Notebook
        #     print(chunk.choices[0].delta.content or "", end="", flush=True)
    
    

