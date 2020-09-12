from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    )
from articles.models import Article
from .serializers import ArticleSerilaizer
"""
ArticleListView
ArticleDetailView
ArticleCreateView
ArticleUpdateView
ArticleDeleteView

"""
class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilaizer   
    
class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilaizer   

class ArticleCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilaizer   

class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilaizer   

class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilaizer   