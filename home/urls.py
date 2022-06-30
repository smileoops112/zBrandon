from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('blog', blog, name='blog'),
    path('about', about, name='about'),
    path('contacts', about, name='contacts'),
    path('gallery', gallery, name='gallery')
]