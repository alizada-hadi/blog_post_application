from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username",  "email", "phone_number"]
    list_display_links = ["username", "email"]
    list_filter = ["email", "username"]
    search_fields = ["username","email"]
