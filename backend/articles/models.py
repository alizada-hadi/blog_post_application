from django.db import models

class Article(models.Model):
    # author = ""
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="photo-%Y/%m%/%d/", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

