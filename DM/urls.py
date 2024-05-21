from django.urls import path
from . import views 

# http://127.0.0.1:8000/       = homapage
# http://127.0.0.1:8000/index = homapage
# http://127.0.0.1:8000/blogs = blogs
# http://127.0.0.1:8000/blogs/3 = blog-details

urlpatterns = [
    path("", views.index, name = "anasayfa"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<str:id>", views.blog_details, name="blog_details"),
    path("Admin", views.Admin, name="Admin"),
    path("Kayıt", views.Kayıt, name="Kayıt"),
]