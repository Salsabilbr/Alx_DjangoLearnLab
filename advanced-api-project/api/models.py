from django.db import models

# Create your models here.
class Author(models.Model):  
   name = models.CharField(max_length=255)
class Book(models.Model):  
   title = models.CharField(max_length=255)  
   publication_year = models.IntegerField()  
   author = models.ForeignKey(Author, on_delete=models.CASCADE)

# models.py  
class Author(models.Model):  
   # ...  
  
   def __str__(self):  
      return self.name  
  
class Book(models.Model):  
   # ...  
  
   def __str__(self):  
      return self.title  
  
# serializers.py  
class BookSerializer(serializers.ModelSerializer):  
   # ...  
  
   def __init__(self, *args, **kwargs):  
      # ...  
      super().__init__(*args, **kwargs)  
  
class AuthorSerializer(serializers.ModelSerializer):  
   # ...  
  
   def __init__(self, *args, **kwargs):  
      # ...  
      super().__init__(*args, **kwargs)

