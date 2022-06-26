from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import Article
from .serializers import ArticleSerializer


@api_view(["GET"])
def article_list_view(request):
    articles = Article.objects.filter(is_published=True)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def article_detail_view(request, article_id):
    article = Article.objects.filter(is_published=True).get(pk=article_id)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)
