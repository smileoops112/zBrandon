from django.db import models


class Post(models.Model):

    email = models.CharField(max_length=50, verbose_name='Почта')
    subject = models.CharField(max_length=100, verbose_name='Тема поста')
    message = models.TextField(verbose_name='Текст')
    image = models.ImageField(blank=True, upload_to='media/', verbose_name='Картинка', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.subject


