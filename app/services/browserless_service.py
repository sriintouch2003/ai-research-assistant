import os
import json
import logging
import requests
from bs4 import BeautifulSoup
from app.services.openai_service import summarize_text

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

BROWSERLESS_API_KEY = os.getenv("BROWSERLESS_API_KEY")

def scrape_website(objective: str, url: str) -> str:
    """
    Scrapes content from a website and summarizes it if the text is too long.
    """
    headers = {'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}
    data = json.dumps({"url": url})
    post_url = f"https://chrome.browserless.io/content?token={BROWSERLESS_API_KEY}"

    try:
        response = requests.post(post_url, headers=headers, data=data, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        text = soup.get_text()

        if len(text) > 10000:
            return summarize_text(objective, text)
        return text
    except requests.RequestException as e:
        logger.error("Scraping failed: %s", e)
        raise RuntimeError("Scraping tool error.")
