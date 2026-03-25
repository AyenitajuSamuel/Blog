from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return HttpResponse(f"There are {posts.count()} posts in this app.")
