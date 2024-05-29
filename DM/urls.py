from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import KayitOlView, YeniKullaniciView

# http://127.0.0.1:8000/       = homapage
# http://127.0.0.1:8000/index = homapage
# http://127.0.0.1:8000/blogs = blogs
# http://127.0.0.1:8000/blogs/3 = blog-details

urlpatterns = [
    path("", views.index, name = "anasayfa"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
    path("Admin", views.Admin, name="Admin"),
    path("Kayıt", views.register, name="Kayıt"),
    path("category/<slug:slug>/", views.blogs_by_category, name="blogs_by_category"),
]