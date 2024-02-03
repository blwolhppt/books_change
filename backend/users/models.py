from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=250,
                              unique=True,
                              blank=False,
                              null=False,
                              verbose_name="Почта")

    username = models.CharField(
        max_length=250,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Никнейм')

    first_name = models.CharField(max_length=250,
                                  blank=False,
                                  null=False,
                                  verbose_name="Имя")

    last_name = models.CharField(max_length=250,
                                 blank=False,
                                 null=False,
                                 verbose_name="Фамилия")

    password = models.CharField(max_length=250,
                                verbose_name="Пароль")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    def __str__(self):
        return self.username
