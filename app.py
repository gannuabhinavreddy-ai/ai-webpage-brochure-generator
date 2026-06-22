#imports
import os
import json 
from IPython.display import Markdown, display, update_display
from scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI


#intialize and constants
MODEL = os.getenv("MODEL_NAME")
openai=OpenAI(base_url=os.getenv("OPENAI_API_BASE"), api_key=os.getenv("OPENAI_API_KEY"))


#system prompt
link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

#user prompt
def get_links_user_prompt(url):
    user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, 
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.
Return only real URLs.
Do not use placeholders.

Links (some might be relative links):

"""
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt


#select relevant links
def select_relevant_links(url):
    print(f"Selecting relevant links for {url} by calling {MODEL}")
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role":"system", "content" : link_system_prompt
            },
            {
                "role":"user", "content" : get_links_user_prompt(url)
            }
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    links = json.loads(result)
    print(f"Found {len(links['links'])} relevant links")
    return links


#fetching content and relevant links
def fetch_page_and_all_relevant_links(url):
    contents= fetch_website_contents(url)
    relevant_links = select_relevant_links(url)
    result = f"##Landing page :\n\n{contents}\n\n ##Relevant links:\n\n"
    for link in relevant_links['links']:
        result += f"### {link['type']} \n\n"
        print(link['url'])
        result += fetch_website_contents(link['url'])
    return result



#brochure system prompt
brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""

# Or uncomment the lines below for a more humorous brochure - this demonstrates how easy it is to incorporate 'tone':

# brochure_system_prompt = """
# You are an assistant that analyzes the contents of several relevant pages from a company website
# and creates a short, humorous, entertaining, witty brochure about the company for prospective customers, investors and recruits.
# Respond in markdown without code blocks.
# Include details of company culture, customers and careers/jobs if you have the information.
# """


#brochure user prompt
def get_brochure_user_prompt(company_name, url):
    user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
Return only real URLs.
Do not use placeholders.
"""
    user_prompt += fetch_page_and_all_relevant_links(url)
    user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
    return user_prompt



#generate brochure
def create_brochure(company_name, url):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role":"system", "content" : brochure_system_prompt
            },
            {
                "role":"user", "content" : get_brochure_user_prompt(company_name, url)
            }
        ],
    )
    result = response.choices[0].message.content
    display(Markdown(result))
    

#calling the function to create brochure for a company
create_brochure("HuggingFace", "https://huggingface.co")



