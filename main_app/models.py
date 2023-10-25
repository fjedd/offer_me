from django.db import models


class Creator(models.Model):
    pass


class JobOffer(models.Model):
    title = models.CharField(max_length=500)
    company = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    is_remote = models.BooleanField()
    salary = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date_posted = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.title