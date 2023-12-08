from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Дополнительные поля, если нужно
    # Например:
    # age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title
