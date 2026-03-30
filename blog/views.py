from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {"posts":posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_details.html', {"post": post})
