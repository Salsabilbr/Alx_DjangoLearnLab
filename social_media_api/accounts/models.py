from django.db import models  
from django.contrib.auth.models import AbstractUser  
  
class User(AbstractUser):  
 bio = models.TextField(blank=True)  
 profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)  
 followers = models.ManyToManyField('self', symmetrical=False, blank=True)
from django.db import models  
from django.contrib.auth.models import User  
  
class Post(models.Model):  
  author = models.ForeignKey(User, on_delete=models.CASCADE)  
  title = models.CharField(max_length=255)  
  content = models.TextField()  
  created_at = models.DateTimeField(auto_now_add=True)  
  updated_at = models.DateTimeField(auto_now=True)  
  
class Comment(models.Model):  
  post = models.ForeignKey(Post, on_delete=models.CASCADE)  
  author = models.ForeignKey(User, on_delete=models.CASCADE)  
  content = models.TextField()  
  created_at = models.DateTimeField(auto_now_add=True)  
  updated_at = models.DateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
# Create your models here.
