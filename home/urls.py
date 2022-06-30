from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('blog', blog, name='blog'),
    path('about', about, name='about'),
    path('contacts', about, name='contacts'),
    path('gallery', gallery, name='gallery'),
    path('post-info', get_info_about_post, name='post_info')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)