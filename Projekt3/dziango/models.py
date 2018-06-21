from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Thread(models.Model):
    poster = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=150)
    date_creation = models.DateTimeField(default=timezone.now)
    last_post = models.DateTimeField(blank=True, null=True)


class Reply(models.Model):
    poster = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)



