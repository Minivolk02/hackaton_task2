from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index_view, name='home'),
    path('ideas/<slug:slug>/', list_ideas, name='idea_item'),
    path('add_idea/', add_idea, name='add_idea'),
    path('ideas/<slug:slug>/add_golos/', add_golos, name='add_golos'),
]
