from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    news_by_title = []
    news = search_news({'title': {'$regex': title, '$options': '-i'}})

    for new in news:
        news_by_title.append((new['title'], new['url']))

    return news_by_title


def search_by_date(date):
    try:
        date_format = datetime.strptime(date, '%Y-%m-%d')

        news_by_date = []
        news = search_news({'timestamp': format(date_format, '%d/%m/%Y')})

        for new in news:
            news_by_date.append((new['title'], new['url']))

        return news_by_date

    except ValueError:
        raise ValueError('Data inválida')


def search_by_tag(tag):
    news_by_tag = []
    news = search_news({'tags': {'$regex': tag, '$options': '-i'}})

    for new in news:
        news_by_tag.append((new['title'], new['url']))

    return news_by_tag


def search_by_category(category):
    news_by_category = []
    news = search_news({'category': {'$regex': category, '$options': '-i'}})

    for new in news:
        news_by_category.append((new['title'], new['url']))

    return news_by_category
