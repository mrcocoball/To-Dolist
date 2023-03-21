from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [

    # Example : /profiles/
    path('', views.main, name="main"),

    # Example: /profiles/{id}/
    path('<int:pk>/', views.detail, name="detail"),

]