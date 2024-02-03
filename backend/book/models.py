from django.db import models

from users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name='Название', unique=True)

    slug = models.SlugField(max_length=150,
                            verbose_name='Cлаг', unique=True)

    class Meta:
        verbose_name = 'Жанры'

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор объявления')
    name = models.CharField(max_length=150,
                            verbose_name='Название')
    writer = models.CharField(max_length=150,
                              verbose_name='Автор произведения')
    genre = models.ManyToManyField(Genre, verbose_name='Тег')
    pub_date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Книги'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name
