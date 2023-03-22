from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from todos.models import Todo
from todolist.views import OwnerOnlyMixin

# ListView
class TodoLV(ListView):

    model = Todo
    context_object_name = 'todos'
    paginate_by = 10
    template_name = 'todos.html'


# DetailView
class TodoDV(DetailView):

    model = Todo
    template_name = 'todos_detail.html'


# CreateView
class TodoCreateView(LoginRequiredMixin, CreateView):

    model = Todo
    fields = ['title', 'description',]
    success_url = reverse_lazy('todos:main')
    template_name = 'todo_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.owner.plus_todo_count()
        return super().form_valid(form)


# UpdateView
class TodoUpdateView(OwnerOnlyMixin, UpdateView):

    model = Todo
    fields = ['title', 'description',]
    template_name = 'todo_form.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# Delete
@require_POST
def delete(request, id):

    db_article = get_object_or_404(Todo, id = id)

    if request.user == db_article.owner:
        db_article.delete()

    return HttpResponseRedirect(reverse('todos:main'))

# Complete
@require_POST
def complete(request, id):

    db_article = get_object_or_404(Todo, id = id)

    if request.user == db_article.owner:
        db_article.change_complete()
        user = db_article.owner

        user.plus_todo_complete_count()

    request_path = request.GET.get('path', None)

    if request_path != None: # 세부 페이지에서 호출 시
        return HttpResponseRedirect(reverse('todos:detail', args=[request_path]))
    else: # 그 외
        return HttpResponseRedirect(reverse('todos:main'))