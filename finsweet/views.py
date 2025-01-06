from django.shortcuts import render, get_object_or_404

from .models import (
    Post, About_us,
    Our_mission, Category,
    Author
)


def index(request):
    post = get_object_or_404(Post, slug="first-post")
    posts = Post.objects.all()
    last_post = Post.objects.last()
    about_us = get_object_or_404(About_us, pk=1)
    our_mission = get_object_or_404(Our_mission, pk=1)
    categories = Category.objects.all()
    authors = Author.objects.all()

    data = {
        "index_header_post": post,
        "posts": posts,
        "last_post": last_post,
        "about_us": about_us,
        "our_mission": our_mission,
        "categories": categories,
        "authors": authors
    }
    return render(request, "index.html", data)


def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    data = {
        "categories": categories,
        "posts": posts,
    }
    return render(request, "blog.html", data)


def blog_single(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    data = {
        "title": post.title,
        "content": post.content,
        "created_date": post.created_date,
        "image": post.image,
        "author": post.author,
        "category": post.category.name,
    }
    return render(request, "single.html", data)


def category(request):
    return render(request, "category.html")


def about_us(request):
    return render(request, "about-us.html")


def contact_us(request):
    return render(request, "contact-us.html")
