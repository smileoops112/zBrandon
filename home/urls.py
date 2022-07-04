from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<pk>', PostDetail.as_view(), name='post-detail'),
    path('blog', blog, name='blog'),
    path('about', about, name='about'),
    path('contacts', about, name='contacts'),
    path('gallery', gallery, name='gallery'),

]
