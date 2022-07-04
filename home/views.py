from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.views import View

from .models import Post
from django.views import generic


class PostList(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'home/index.html'


class PostDetail(generic.DetailView):
    model = Post


def post_detail_view(request, pk):
    try:
        post_id = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404('Нету такого поста')
    return render(request, 'home/post_info.html', context={'post_id': post_id})


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