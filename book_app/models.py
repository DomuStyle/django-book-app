from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50, default="No title defined")
    author = models.CharField(max_length=25, default="No author defined")
    price = models.DecimalField(max_digits=8, decimal_places=2)