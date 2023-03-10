from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    nickname = models.CharField('NICKNAME', max_length=20, unique=True, null=True)
    first_name = None
    last_name = None
    todo_count = models.BigIntegerField('TODO_COUNT', null=True)
    todo_complete_count = models.BigIntegerField('TODO_COMPLETE_COUNT', null=True)

    def __str__(self):
        return self.email
