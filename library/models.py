from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.TextField(max_length=2000, null = True, blank = True)
    isbn = models.TextField(max_length=2000, null = True, blank = True)
    authors = models.JSONField(null=True, blank=True)
    number_of_pages = models.IntegerField(null=True, blank=True)
    publisher = models.TextField(max_length=2000, null = True, blank = True)
    country = models.TextField(max_length=2000, null = True, blank = True)
    release_date = models.DateField(null = True, blank = True)
