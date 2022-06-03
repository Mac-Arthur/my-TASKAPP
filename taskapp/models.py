from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task = models.CharField(max_length=120)
    iscomplete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.task
    