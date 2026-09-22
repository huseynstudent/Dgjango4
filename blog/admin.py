from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)

@admin.register(Post)                                  # register-in decorator forması — Dərs 2
class PostAdmin(admin.ModelAdmin):                     # ModelAdmin-dən törəyir
    list_display = ["title", "author", "is_published", "views"]   # sütunlar
    list_filter = ["is_published", "category","created_at"]       # sağda filtr paneli
    search_fields = ["title", "content", "author"]                       # axtarış qutusu