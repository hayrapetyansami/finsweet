from django.urls import path

from .views import (
    index, blog,
    about_us, contact_us,
    blog_single, category
)

urlpatterns = [
    path("", index, name="index"),
    path("blog/", blog, name="blog"),
    path("blog/<slug:post_slug>/", blog_single, name="single"),
    path("category/", category, name="category"),
    path("about-us/", about_us, name="about-us"),
    path("contact-us/", contact_us, name="contact-us"),
]
