from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status
from apps.core.utils.context_articles import get_context_from_content

from apps.core.utils.endpoints.new_api_urls import set_url_article


class TOPArticles(APIView):

    def get(self, request):
        result = requests.get(set_url_article('us'))
        content = result.json()
        articles = content['articles']

        context = get_context_from_content(articles)

        return Response(context, status=status.HTTP_200_OK)
