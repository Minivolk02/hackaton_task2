from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    path = 'photos/%s/%s' % (instance.user.username, filename)
    return path

class Position(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название должности')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title

class UserProfile(AbstractUser):
    username = models.CharField(max_length=256, verbose_name='Логин', unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата Рождения')
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Аватар')
    gamefication = models.IntegerField(blank=True, null=True)
    user_position = models.ForeignKey(Position, models.CASCADE, verbose_name='Должность пользователя', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'middle_name', 'birth_date']
