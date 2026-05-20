from django.contrib import admin

from .models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "breed", "birth_year", "color", "created_at")
    list_filter = ("breed", "color", "birth_year", "created_at")
    search_fields = ("name", "owner__username", "breed", "color")
