from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   published_date = models.DateTimeField(auto_now_add=True)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)  
   updated_at = models.DateTimeField(auto_now=True)

["Comment(models.Model)"]

from django.db import models

class Tag(models.Model):
   name = models.CharField(max_length=255)

from django.db import models  
  
class Post(models.Model):  
   tags = models.ManyToManyField(Tag)

# Create your models here.
