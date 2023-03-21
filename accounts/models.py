from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    first_name = None
    last_name = None
    todo_count = models.BigIntegerField('TODO_COUNT', null=True, default=0)
    todo_complete_count = models.BigIntegerField('TODO_COMPLETE_COUNT', null=True, default=0)

    def __str__(self):
        return self.email
    
    def plus_todo_count(self):
        self.todo_count += 1
        self.save()

    def plus_todo_complete_count(self):
        self.todo_complete_count += 1
        self.save()

