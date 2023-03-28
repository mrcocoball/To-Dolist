from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('todos/', include('todos.urls')),
    path('', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
]

if settings.DEBUG is False:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
    ]