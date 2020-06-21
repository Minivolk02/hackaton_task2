from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth import get_user_model
from vote.models import VoteModel
from accounts.models import Department
from django_comments_xtd.models import XtdComment
User = get_user_model()


class CommentOwnModel(XtdComment):
    commentary = models.CharField(verbose_name='Комментарий', max_length=500)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'


class Idea(VoteModel, models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name='Отправитель', blank=True, unique=False, default=1)
    title = models.CharField(max_length=100, verbose_name='Название идеи')
    slug = models.SlugField(max_length=100, verbose_name='Тэг идеи')
    content = RichTextUploadingField(verbose_name='Контент идеи')
    date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now, blank=True)
    is_published = models.BooleanField(verbose_name='Опубликовано?', default=True)
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры', blank=True)
    question = models.CharField(max_length=100, verbose_name='Вопрос', null=True)
    groups = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='ideas/', verbose_name='Фото', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('idea_item', kwargs={'slug': self.slug})

    def get_username(self):
        return self.user.username

    def get_score(self):
        return self.votes.count()

    get_score.short_description = 'Количество голосов'

    def check_votes(self, request):
        return self.votes.exists(request.user.id)

    get_username.short_description = 'Отправитель'

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'
