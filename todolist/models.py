from django.db import models


class Task(models.Model):
    name = models.CharField('Nome', max_length=255)
    status = models.CharField(
        choices=(('todo', 'TODO'), ('done', 'Done')),
        max_length=4,
        default='todo'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
