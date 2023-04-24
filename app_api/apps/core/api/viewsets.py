
from rest_framework import viewsets

from apps.core.api.views import TOPArticles


class TOPArticlesViewSet(viewsets.ViewSet):

    def list(self, request):
        view = TOPArticles.as_view()
        return view(request._request)
