from django.db import models

# Create your models here.

class Post(models.Model):
    # Suc ve Ceza
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_at"] # yeni postlar yuxarıda görünsün

    def __str__(self):
        return self.title # Object 132214