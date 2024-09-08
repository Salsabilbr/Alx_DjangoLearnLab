from rest_framework import serializers  
from .models import Book, Author  
  
class BookSerializer(serializers.ModelSerializer):  
   class Meta:  
      model = Book  
      fields = '__all__'  
  
class AuthorSerializer(serializers.ModelSerializer):  
   books = BookSerializer(many=True, read_only=True)  
  
   class Meta:  
      model = Author  
      fields = ['name', 'books']

class BookSerializer(serializers.ModelSerializer):  
   ...  
  
   def validate_publication_year(self, value):  
      if value > datetime.date.today().year:  
        raise serializers.ValidationError('Publication year cannot be in the future')  
      return value

# serializers.py  
class AuthorSerializer(serializers.ModelSerializer):  
   # ...  
  
   def get_books(self, obj):  
      return BookSerializer(obj.books, many=True).data

