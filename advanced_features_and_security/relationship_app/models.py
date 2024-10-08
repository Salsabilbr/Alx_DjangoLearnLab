from django.db import models

class Author(models.Model):
   name = models.CharField(max_length=255)
   return self.name

class Book(models.Model):
   title = models.CharField(max_length=255)
   author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
   name = models.CharField(max_length=255)
   books = models.ManyToManyField(Book)

class Librarian(models.Model):
   name = models.CharField(max_length=255)
   library = models.OneToOneField(Library, on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import get_user_model  
  
class Profile(models.Model):  
   user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

from django.db import models  
from django.contrib.auth.models import User  
  
class UserProfile(models.Model):  
   user = models.OneToOneField(User, on_delete=models.CASCADE)  
   role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])
  
from django.db.models.signals import post_save  
from django.contrib.auth.models import User  
from django.dispatch import receiver  

@receiver(post_save, sender=User)  
def create_user_profile(sender, instance, created, **kwargs):  
   if created:  
      UserProfile.objects.create(user=instance)  
  
@receiver(post_save, sender=User)  
def save_user_profile(sender, instance, **kwargs):  
      instance.userprofile.save()

from django.db import models

class Book(models.Model):
   title = models.CharField(max_length=200)
   author = models.CharField(max_length=100)
   publication_date = models.DateField()

   class Meta:
      permissions = (
        ('can_add_book', 'Can add book'),
        ('can_change_book', 'Can change book'),
        ('can_delete_book', 'Can delete book'),
      )
