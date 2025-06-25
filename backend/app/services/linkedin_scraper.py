import time
import requests
from bs4 import BeautifulSoup
from app.utils.exceptions import ScrapeError
from app.config import config

def scrape_profiles(company_url: str) -> list[dict]:
    time.sleep(config.scraper.delay_seconds)
    resp = requests.get(company_url)
    if resp.status_code != 200:
        raise ScrapeError(f"Fout bij ophalen {company_url}")
    soup = BeautifulSoup(resp.text, "html.parser")
    return []
