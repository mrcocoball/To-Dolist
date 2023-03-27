from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from todos.models import Todo
from todolist.views import OwnerOnlyMixin
from django.db.models.query_utils import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime, timedelta

# ListView
class TodoLV(ListView):

    model = Todo
    context_object_name = 'todos'
    paginate_by = 10
    block_size = 5 # 하단 페이지 목록 수
    template_name = 'todos.html'

    def get_queryset(self):

        # 동적 쿼리

        search_type = self.request.GET.get("searchType", "")
        keyword = self.request.GET.get("keyword", "")
        start_date = self.request.GET.get("startDate", "")
        target_date = self.request.GET.get("targetDate", "")

        q = Q()

        if search_type:
            if search_type == "title": # 제목 검색
                if keyword:
                    q.add(Q(title__contains=keyword), q.AND)
                if start_date:
                    if target_date:
                        convert_date = datetime.strptime(target_date, "%Y-%m-%d").date() + timedelta(days=1) # target_date에 하루 추가
                        q.add(Q(created_at__gte=start_date, created_at__lte=convert_date), q.AND)
                    else:
                        q.add(Q(created_at__gte=start_date), q.AND)
                else:
                    if target_date:
                        convert_date = datetime.strptime(target_date, "%Y-%m-%d").date() + timedelta(days=1) # target_date에 하루 추가
                        q.add(Q(created_at__lte=convert_date), q.AND)
            if search_type == "description": # 본문 검색
                if keyword:
                    q.add(Q(description__contains=keyword), q.AND)
                if start_date:
                    if target_date:
                        convert_date = datetime.strptime(target_date, "%Y-%m-%d").date() + timedelta(days=1) # target_date에 하루 추가
                        q.add(Q(created_at__gte=start_date, created_at__lte=convert_date), q.AND)
                    else:
                        q.add(Q(created_at__gte=start_date), q.AND)
                else:
                    if target_date:
                        convert_date = datetime.strptime(target_date, "%Y-%m-%d").date() + timedelta(days=1) # target_date에 하루 추가
                        q.add(Q(created_at__lte=convert_date), q.AND)

        if self.request.user.is_authenticated:
            return Todo.objects.filter(owner=self.request.user).filter(q)
        else:
            return [] # AnonymousUser는 빈 리스트 노출
    
        
    def get_context_data(self, **kwargs):
        search_type = self.request.GET.get("searchType", "")
        keyword = self.request.GET.get("keyword", "")
        start_date = self.request.GET.get("startDate", "")
        target_date = self.request.GET.get("targetDate", "")

        context = super().get_context_data(**kwargs)

        context['st'] = search_type
        context['k'] = keyword
        context['s'] = start_date
        context['t'] = target_date

        # 하단 페이지 수 조정
        start_index = int((context['page_obj'].number - 1) / self.block_size) * self.block_size
        end_index = min(start_index + self.block_size, len(context['paginator'].page_range))

        context['page_range'] = context['paginator'].page_range[start_index:end_index]

        return context
    

# DetailView
class TodoDV(OwnerOnlyMixin, DetailView):

    model = Todo
    template_name = 'todos_detail.html'

# DetailView
class TodoShareDV(DetailView):

    model = Todo
    template_name = 'todos_detail_share.html'


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