# BrochureAI

## Overview
BrochureAI is a Python application that leverages Large Language Models (LLMs) to automatically generate engaging, informative brochures for companies based on their website content. It scrapes the landing page and relevant subpages, then uses an LLM (such as OpenAI's GPT models) to craft a professional marketing brochure in Markdown format.

## Features
- **Automated Web Scraping:** Extracts content and links from company websites using BeautifulSoup and requests.
- **Intelligent Link Filtering:** Uses LLMs to identify and select only the most relevant pages (e.g., About, Careers, Services) for brochure content.
- **Brochure Generation:** Creates a concise, well-structured brochure in Markdown, highlighting company mission, values, products/services, and career opportunities.
- **Markdown File Output:** Automatically writes the generated brochure content to a `.md` file for easy sharing and further editing.
- **Flexible LLM Provider Support:** Works with OpenAI and can be extended to other providers by specifying base URLs and models.

## How It Works
1. **User Input:** Enter the company name, website URL, LLM provider, API key, and model via the CLI.
2. **Scraping:** The app fetches the landing page and all links, then uses the LLM to filter for relevant subpages.
3. **Content Extraction:** Scrapes the text content from the landing page and selected subpages.
4. **Brochure Creation:** Sends the content to the LLM, which returns a Markdown-formatted brochure.
5. **Output:** The generated brochure is saved as a Markdown (`.md`) file in your project directory for easy access and sharing.

## Installation
1. **Clone the repository:**
	```
	git clone https://github.com/Narenpradhan/Company-Brochure-Generator.git
	cd Company-Brochure-Generator
	```
2. **Install dependencies:**
	```
	uv sync
	```
3. **Activate virtual environment**
    ``` 
    # On Windows:
    .venv\Scripts\activate
    ```

    ```
    # On macOS/Linux:
    source .venv/bin/activate
    ```

## Usage
Run the application from the command line:
```
python src/main.py
```
The application will scrape the website, filter relevant links, and generate a Markdown brochure using the selected LLM.

## Project Structure
```
Company-Brochure-Generator/
├── src/
│   ├── main.py                # CLI entry point
│   ├── brochure_generator.py  # Brochure generation logic
│   └── scraper.py             # Web scraping utilities
├── requirements.txt           # Python dependencies
├── pyproject.toml             # Project metadata
├── README.md                  # Project documentation
```

## Dependencies
- [openai](https://pypi.org/project/openai/) - For LLM API access
- [python-dotenv](https://pypi.org/project/python-dotenv/) - For environment variable management
- [requests](https://pypi.org/project/requests/) - For HTTP requests
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - For HTML parsing
- [IPython](https://pypi.org/project/ipython/) - For Markdown display (optional, Jupyter only)

