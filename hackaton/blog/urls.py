from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('ideas/<slug:slug>/', ListIdeas.as_view(), name='idea_item'),
    path('add_idea/', add_idea, name='add_idea'),
    path('add_golos/', add_golos, name='add_golos'),
]
