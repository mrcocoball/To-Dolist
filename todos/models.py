from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Todo(models.Model):

    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="WRITER")
    description = models.CharField('DESCRIPTION', max_length=100)
    created_at = models.DateField('CREATED_AT', auto_now_add=True)
    modified_at = models.DateField('MODIFIED_AT', auto_now=True)
    is_complete = models.BooleanField('IS_COMPLETE', default=False)

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'
        db_table = 'todos_todos'
        ordering = ('-created_at',)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('todos:todo_detail')
    
    def get_previous(self):
        return self.get_previous_by_created_at()
    
    def get_next(self):
        return self.get_next_by_created_at()