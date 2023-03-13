from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [

    # Example : /todos/
    path('', views.TodoLV.as_view(), name="main"),

    # Example: /todos/{id}/
    path('<int:pk>/', views.TodoDV.as_view(), name="detail"),

    # Example : /todos/write/
    path('write/', views.TodoCreateView.as_view(), name="write"),

    # Example : /todos/{id}/modify/
    path('<int:pk>/modify/', views.TodoUpdateView.as_view(), name="modify"),

    # Example : /todos/{id}/delete/
    path('<int:pk>/delete/', views.delete, name="delete"),

    # Example : /todos/{id}/complete
    path('<int:pk>/complete/', views.complete, name="complete"),

]