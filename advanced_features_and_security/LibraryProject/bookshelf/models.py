from django.db import models

# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=200)
   author = models.CharField(max_length=100)
   publication_year = models.IntegerField()

from django.contrib.auth.models import AbstractUser  
from django.db import models  
  
class CustomUser(AbstractUser):
   date_of_birth = models.DateField(null=True, blank=True)  
   profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
   def create_user(self, username, email, password, **extra_fields):
      pass

   def create_superuser(self, username, email, password, **extra_fields):
      pass

from django.db import models  
  
class Message(models.Model):  
   title = models.CharField(max_length=200)  
   author = models.CharField(max_length=100)  
  
   class Meta:  
      permissions = (  
        ('can_view', 'Can view'),  
        ('can_create', 'Can create'),  
        ('can_edit', 'Can edit'),  
        ('can_delete', 'Can delete'),
        ('can_create', 'can_delete'),              
      )
