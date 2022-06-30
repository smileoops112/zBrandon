from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def about(requst):
    return render(requst, 'home/about.html')


def blog(requst):
    return render(requst, 'home/blog.html')


def contacts(requst):
    return render(requst, 'home/contacts.html')


def gallery(requst):
    return render(requst, 'home/gallery.html')