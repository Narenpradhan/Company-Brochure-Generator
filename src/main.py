import getpass
import os
from dotenv import load_dotenv
from openai import OpenAI, base_url
from brochure_generator import BrochureGenerator

load_dotenv(override=True)

def main():
    print("----------Welcome to the Company Brochure Generator!----------")
    while True:
        company_name = input("\n\n[*] Enter the Company Name (or type 'exit' to quit): ")
        if company_name.lower() == 'exit':
            print("[*] Exiting the Brochure Generator. Goodbye!")
            break
        
        company_url = input("[*] Enter the Company Website URL: ")

        llm_provider_base_url = 'https://api.openai.com/v1/'
        llm_provider = input("[*] Enter LLM Provider (default: OpenAI): ") or "openai"
        if not llm_provider.lower() == "openai":
            llm_provider_base_url = input("[*] Enter the Base URL: ")
        llm_api_key = getpass.getpass("[*] Enter the API Key: ")
        llm_model = input("[*] Enter the LLM Model: ")
        
        brochure_generator = BrochureGenerator(llm_api_key, llm_provider_base_url, llm_model)
        brochure_content = brochure_generator.create_brochure(company_name, company_url)

        print(f"\nWriting brochure content to file {company_name}_brochure.md...")
        with open(f"{company_name}_brochure.md", "w", encoding="utf-8") as f:
            f.write(brochure_content)


if __name__ == "__main__":
    main()

