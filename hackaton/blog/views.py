from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class IndexView(ListView):
    paginate_by = 3
    model = Idea
    template_name = 'crm/index.html'
    context_object_name = 'idea'

    def get_queryset(self):
        return Idea.objects.filter(is_published=True)



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