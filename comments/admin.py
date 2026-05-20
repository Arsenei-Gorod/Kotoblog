from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "author", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("text", "author__username", "post__title")
