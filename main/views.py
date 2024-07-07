from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Post, Comment


def base(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'base.html', context=context)


def detail(request, postid):
    post = get_object_or_404(Post, id=postid)
    comments = post.comments.all()
    posts = Post.objects.all()


    context = {
        'post': post,
        'comments': comments,
        'posts': posts,
    }
    return render(request, 'video-page.html', context=context)