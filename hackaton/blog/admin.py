from django.contrib import admin
from .models import *
from .forms import *


class IdeaAdmin(admin.ModelAdmin):
    form = IdeaAdminForm
    list_display = ('id', 'get_username', 'title', 'date', 'is_published', 'get_score')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'get_username', 'title')
    fields = ('get_username', 'title', 'slug', 'content', 'date', 'is_published', 'get_score', 'tags')
    readonly_fields = ('get_username', 'get_score')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')


admin.site.register(Idea, IdeaAdmin)