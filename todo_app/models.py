from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'], name='unique_user_title')
        ]

    def __str__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Pending'}"
