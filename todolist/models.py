from django.db import models
from datetime import datetime


class TodoItem(models.Model):
    title = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at=models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if self.is_completed==1:
            self.completed_at=datetime.now()    
        return super(TodoItem,self).save(*args,**kwargs)
   
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todolist_items'
