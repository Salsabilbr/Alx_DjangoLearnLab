from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
   title = models.CharField(max_length=200)
   author = models.CharField(max_length=100)
