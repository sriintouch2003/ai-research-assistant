import os
import json
import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def search(query: str) -> str:
    """
    Performs a search query using the Serper API.
    """
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        response.raise_for_status()
        logger.info("Search successful for query: %s", query)
        return response.text
    except requests.RequestException as e:
        logger.error("Search failed: %s", e)
        raise RuntimeError("Search tool error.")
