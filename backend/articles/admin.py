from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "created", "updated", "is_published"]
    list_filter = ("title", "author", "created")
    list_display_links = ("title", "author")
    search_fields = ["title"]
    list_per_page = 25


admin.site.register(Article, ArticleAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "body", "created"]


