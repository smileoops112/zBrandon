from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'home/index.html', context={'posts': posts})


def get_info_about_post(request):
    return render(request, 'home/post_info.html')


def about(requst):
    return render(requst, 'home/about.html')


def blog(requst):
    return render(requst, 'home/blog.html')


def contacts(requst):
    return render(requst, 'home/contacts.html')


def gallery(requst):
    return render(requst, 'home/gallery.html')