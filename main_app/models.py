from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        permissions = (
            ('Moderator', 'Moderator'),
            ('Creator', 'Creator'), ('Viewer', 'Viewer'),
        )


class JobOffer(models.Model):
    title = models.CharField(max_length=500)
    company = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    is_remote = models.CharField(
        max_length=20, choices=[
            ('Remote', 'Remote'),
            ('Hybrid', 'Hybrid'),
            ('Office', 'Office'),
        ],
        default='Remote',
    )
    salary = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date_posted = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=500)
