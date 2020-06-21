from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from .models import *
from accounts.models import *
from django.template.defaultfilters import slugify
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index_view(request):
    form = SearchIdea()
    departments = Department.objects.all()
    if request.method == 'POST':
        form = SearchIdea(request.POST)
        if form.is_valid():
            tags = Idea.objects.filter(content__icontains=form.cleaned_data['search'])
            return render(request, 'crm/index.html', {'idea': tags, 'form': form, 'departs': departments})

    else:
        if request.GET.get('groups'):
            group = request.GET.get('groups')
            data = Idea.objects.filter(groups__title=group)
            return render(request, 'crm/index.html', {'idea': data, 'departs': departments, 'form':form})
        ideas = Idea.objects.filter(is_published=True)
        paginator = Paginator(ideas, 2)
        page_number = request.GET.get('page')
        ideas = paginator.get_page(page_number)

        return render(request, 'crm/index.html', {'idea': ideas, 'form': form, 'departs': departments})


def list_ideas(request, slug):
    data = Idea.objects.get(slug=slug)
    data.views = data.views + 1
    data.save()
    return render(request, 'crm/idea_item.html', {'idea_item': data})


@login_required
def add_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = IdeaForm()
    return render(request, 'crm/add_idea.html', {'form': form})


@login_required
def add_golos(request, slug):
    if request.method == 'POST':
        form = IdeaForm()
        golos = Idea.objects.get(slug=slug)
        golos.votes.up(request.user.id)
        golos.save()
        return redirect('home')
