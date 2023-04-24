from django.conf import settings

BASE_URL = settings.BASE_URL
NEW_API_KEY = settings.NEW_API_KEY

PATH_ARTICLE = "top-headlines"

BASE_URL_ARTICLE = F"{BASE_URL}/{PATH_ARTICLE}?country=%s&apiKey={NEW_API_KEY}"


def set_url_article(lang='pt'):
    return BASE_URL_ARTICLE % lang
