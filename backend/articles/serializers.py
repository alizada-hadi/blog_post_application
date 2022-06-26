from rest_framework import serializers
from .models import  Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)
    author = serializers.RelatedField(source="user.username", read_only=True)
    class Meta:
        model = Article
        fields = ["id", "title", "author", "body", "is_published", "created", "updated", "comments"]

    def get_comments(self, obj):
        comments = obj.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data


