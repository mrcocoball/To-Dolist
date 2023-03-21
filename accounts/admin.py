from django.contrib import admin
#from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)