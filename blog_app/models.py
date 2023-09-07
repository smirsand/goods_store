from django.db import models


class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, unique=True, verbose_name='slug')
    content = models.TextField(verbose_name='content')
    image = models.ImageField(verbose_name='изображение', blank=True, null=True)
    date_of_creation = models.DateTimeField(verbose_name='дата создания', blank=True, null=True)
    sign_of_publication = models.BooleanField(verbose_name='признак публикации', blank=True, null=True)
    number_of_views = models.IntegerField(verbose_name='количество просмотров', blank=True, null=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
