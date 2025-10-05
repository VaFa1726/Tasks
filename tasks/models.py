from django.db import models
from django.utils import timezone
from datetime import timedelta

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'Not Started'),
        ('doing', 'In Progress'),
        ('done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    notify = models.BooleanField(default=True)

    class Meta:
        ordering = ['priority', 'due_date']

    def __str__(self):
        return self.title

    def is_due_soon(self):
        if not self.due_date or not self.notify:
            return False
        now = timezone.now()
        diff = self.due_date - now
        return timedelta(hours=0) <= diff <= timedelta(hours=24)
