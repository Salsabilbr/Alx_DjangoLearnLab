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
# Create your models here.
