import time
import requests
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
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


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css('a.cs-overlay-link::attr(href)').getall()


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css('a.next.page-numbers::attr(href)').get()


def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()

    title = selector.css('h1.entry-title::text').get().strip()

    timestamp = selector.css('li.meta-date::text').get()

    writer = selector.css('span.author a::text').get().strip()

    comments_count = selector.css(
        'h5.title-block ol.comment-list li'
        ).getall().__len__() or 0

    summary = ''.join(selector.css(
        'div.entry-content p'
        )[0].xpath('.//text()').getall()).strip()

    tags = selector.css('section.post-tags ul li a::text').getall()

    category = selector.css('a.category-style span.label::text').get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category
    }


def get_tech_news(amount):
    tech_news = []
    base_url = 'https://blog.betrybe.com'

    while len(tech_news) < amount:
        for url in scrape_novidades(fetch(base_url)):
            if amount > len(tech_news):
                tech_news.append(scrape_noticia(fetch(url)))

        base_url = scrape_next_page_link(fetch(base_url))

    create_news(tech_news)

    return tech_news
