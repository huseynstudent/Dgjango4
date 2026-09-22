from django.http import Http404
from django.shortcuts import render

# from .data import POSTS, CATEGORIES

from django.shortcuts import render, get_object_or_404
from .models import Post


# def post_list(request):
#     context = {"posts": POSTS}                       # context = adi dict
#     return render(request, "blog/post_list.html", context)

def post_list(request):
    posts = Post.objects.filter(is_published=True)  # yalnız dərc olunmuş postlar
    # posts = Post.objects.all()  butun postlari gostermek istesek
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)


# def post_detail(request, post_id):
#     for post in POSTS:
#         if post["id"] == post_id:
#             return render(request, "blog/post_detail.html", {"post": post})
#     raise Http404("Belə post yoxdur")

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    return render(request, "blog/post_detail.html", {"post": post})


def about(request):
    return render(request, "blog/about.html")        # context lazım deyilsə, yazmırıq


# ───────────────────────── [PRAKTİKA 8] ─────────────────────────

def category_list(request):
    return render(request, "blog/category_list.html", {"categories": CATEGORIES})


def category_detail(request, slug):
    for category in CATEGORIES:
        if category["slug"] == slug:
            posts = []
            for post in POSTS:
                if post["category"] == slug:
                    posts.append(post)
            context = {"category": category, "posts": posts}
            return render(request, "blog/category_detail.html", context)
    raise Http404("Belə kateqoriya yoxdur")


# ─────────────────────────── [EV 8] ───────────────────────────

def contact(request):                                             # tapşırıq 1
    return render(request, "blog/contact.html")


def author_posts(request, name):                                  # tapşırıq 2
    posts = []
    for post in POSTS:
        if post["author"] == name:
            posts.append(post)
    context = {"name": name, "posts": posts}          # boşdursa template {% empty %} göstərir
    return render(request, "blog/author_posts.html", context)


def latest(request):                                              # tapşırıq 3
    return render(request, "blog/latest.html", {"posts": POSTS[-3:]})


def stats(request):                                               # tapşırıq 4
    context = {"posts": POSTS, "categories": CATEGORIES}
    return render(request, "blog/stats.html", context)
