# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class FileLog(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title