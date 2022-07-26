from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_by_title = []
    news = search_news({'title': {'$regex': title, '$options': '-i'}})

    for new in news:
        news_by_title.append((new['title'], new['url']))

    return news_by_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    news_by_tag = []
    news = search_news({'tags': {'$regex': tag, '$options': '-i'}})

    for new in news:
        news_by_tag.append((new['title'], new['url']))

    return news_by_tag


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
