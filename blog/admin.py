from django.contrib import admin
from .models import Category, Post

# Register your models here.
# admin.site.register(Post)

@admin.register(Post)                                  # register-in decorator forması — Dərs 2
class PostAdmin(admin.ModelAdmin):                     # ModelAdmin-dən törəyir
    list_display = ["title", "author", "is_published", "is_featured", "views"]   # sütunlar
    list_editable = ["is_published", "is_featured"]
    list_filter = ["is_published", "is_featured", "category", "created_at"]       # sağda filtr paneli
    search_fields = ["title", "content", "author"]                       # axtarış qutusu


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "description"]