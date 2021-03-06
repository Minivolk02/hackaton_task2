# Generated by Django 3.0.7 on 2020-06-20 23:10

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('title', models.CharField(max_length=50, verbose_name='Название идеи')),
                ('slug', models.SlugField(max_length=10, verbose_name='Тэг идеи')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент идеи')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('views', models.PositiveIntegerField(blank=True, default=0, verbose_name='Просмотры')),
                ('user', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Идея',
                'verbose_name_plural': 'Идеи',
            },
        ),
    ]
