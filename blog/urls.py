from django.urls import path

from . import views

app_name = "blog"       # ad sahəsi: reverse("blog:post_detail") — başqa app-ın adları ilə qarışmır

urlpatterns = [
    # [DƏRS 7]
    path("", views.post_list, name="post_list"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("about/", views.about, name="about"),

    # [EV 7] — Dərs 8-də bunların template-lərini tələbə yazır (praktika + ev)
    path("contact/", views.contact, name="contact"),
    path("categories/", views.category_list, name="category_list"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("author/<str:name>/", views.author_posts, name="author_posts"),     # Dərs 7-də bonus idi
    path("stats/", views.stats, name="stats"),                              # Dərs 7-də bonus idi

    # [EV 8] yeni səhifə
    path("latest/", views.latest, name="latest"),
]
