from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_list_view, name="article-list"), 
    path("<str:article_id>/", views.article_detail_view, name="article-detail")
]