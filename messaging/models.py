import datetime

import django.utils.timezone
from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.username, self.password


class Messages(models.Model):
    sender = models.CharField(max_length=50)
    recipient = models.CharField(max_length=50)
    message = models.TextField()
    date_created = models.DateTimeField(default=django.utils.timezone.now())

    # def __str__(self):
    #     return self.user_id, self.user_id, self.message
