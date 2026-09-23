from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Category, Post


def post_list(request):
    posts = Post.objects.filter(is_published=True)  # yalnız dərc olunmuş postlar
    # posts = Post.objects.all()  butun postlari gostermek istesek
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    post.views += 1
    post.save(update_fields=["views"])
    return render(request, "blog/post_detail.html", {"post": post})


def about(request):
    return render(request, "blog/about.html")        # context lazım deyilsə, yazmırıq


# ───────────────────────── [PRAKTİKA 8] ─────────────────────────

def category_list(request):
    categories = Category.objects.all()
    return render(request, "blog/category_list.html", {"categories": categories})


def category_detail(request, slug):
    category = Category.objects.filter(slug=slug).first()
    if category is None:
        raise Http404("Belə kateqoriya yoxdur")
    posts = Post.objects.filter(category=category, is_published=True)
    return render(request, "blog/category_detail.html", {"category": category, "posts": posts})


# ─────────────────────────── [EV 8] ───────────────────────────

def contact(request):                                             # tapşırıq 1
    return render(request, "blog/contact.html")


def author_posts(request, name):                                  # tapşırıq 2
    posts = Post.objects.filter(author=name, is_published=True)
    context = {"name": name, "posts": posts}          # boşdursa template {% empty %} göstərir
    return render(request, "blog/author_posts.html", context)


def latest(request):                                              # tapşırıq 3
    posts = Post.objects.filter(is_published=True).order_by("-created_at")[:3]
    return render(request, "blog/latest.html", {"posts": posts})


def stats(request):                                               # tapşırıq 4
    context = {
        "posts": Post.objects.filter(is_published=True).count(),
        "categories": Category.objects.count(),
        "top_post": Post.objects.filter(is_published=True).order_by("-views").first(),
    }
    return render(request, "blog/stats.html", context)
