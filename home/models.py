from django.db import models
from django.urls import reverse


class Post(models.Model):

    email = models.CharField(max_length=50, verbose_name='Почта')
    subject = models.CharField(max_length=100, verbose_name='Тема поста')
    message = models.TextField(verbose_name='Текст')
    url = models.SlugField(null=True)
    image = models.ImageField(blank=True, upload_to='media/', verbose_name='Картинка', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('post_info', args=[str(self.id)])


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.subject


