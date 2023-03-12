from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from todos.models import Todo

# ListView
class TodoLV(ListView):

    model = Todo
    context_object_name = 'todos'
    paginate_by = 10


# DetailView
class TodoDV(DetailView):

    model = Todo


# CreateView
class TodoCreateView(CreateView):

    model = Todo


# UpdateView
class TodoUpdateView(UpdateView):

    model = Todo
    

# etc

def delete(request, idx):

    db_article = Todo.objects.get(id = idx)
    db_article.delete()

def complete(request, idx):

    db_article = Todo.objects.get(id = idx)