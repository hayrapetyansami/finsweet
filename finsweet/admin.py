from django.contrib import admin
from .models import (
    Post, Category,
    Author, About_us,
    Our_mission
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category", "author", "slug"]
    list_display_links = ["id", "title"]
    list_filter = ["title", "author"]
    search_fields = ["title", "author", "category"]
    search_help_text = "You can search only with title, author or category"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    list_filter = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    search_help_text = "You can search only with category name"


@admin.register(About_us)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
    list_display_links = ["title"]


@admin.register(Our_mission)
class OurMissionAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
    list_display_links = ["title"]
