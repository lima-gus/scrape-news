import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )

        if response.status_code == 200:
            return response.text
        else:
            return None

    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css('a.cs-overlay-link::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css('a.next.page-numbers::attr(href)').get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
