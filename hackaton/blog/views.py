from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from .models import *
from django.core.paginator import Paginator
from django.template.defaultfilters import slugify
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index_view(request):
    ideas = Idea.objects.filter(is_published=True)

    paginator = Paginator(ideas, 3)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'crm/index.html', {'page_obj': page_obj, 'idea': ideas})


class ListIdeas(DetailView):
    model = Idea
    template_name = 'crm/idea_item.html'
    context_object_name = 'idea_item'


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
def add_golos(request):
    if request.method == 'POST':
        form = IdeaForm()
        golos = Idea.objects.get(slug=request.POST['golos'])
        golos.votes.up(request.user.id)
        golos.save()
        return redirect('home')
