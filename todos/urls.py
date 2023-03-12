from django.urls import path
from todos import views

app_name = 'todos'
url_patterns = [

    # Example : /todos/
    path('', views.TodoLV.as_view(), name='index'),

    # Example : /todos/write/
    path('write/', views.TodoCreateView.as_view(), name="write"),

    # Example : /todos/{id}/modify/
    path('<int:pk>/modify/', views.TodoUpdateView.as_view(), name="modify"),

    # Example : /todos/{id}/delete/
    path('<int:pk>/delete/', views.delete, name="delete"),

    # Example : /todos/{id}/complete
    path('<int:pk>/complete/', views.complete, name="complete"),

]