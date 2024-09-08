from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book

class BookListView(generics.ListAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
    4. Define a BookDetailView that inherits from generics.RetrieveAPIView to handle retrieving a single book by ID: 

class BookDetailView(generics.RetrieveAPIView):  
   queryset = Book.objects.all()  
   serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):  
   queryset = Book.objects.all()  
   serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):  
   ...  
  
   def perform_create(self, serializer):  
      # Add custom logic here, e.g., send an email notification  
      serializer.save()  
  
class BookUpdateView(generics.UpdateAPIView):  
   ...  
  
   def perform_update(self, serializer):  
      # Add custom logic here, e.g., update related models  
      serializer.save()

class BookListView(generics.ListAPIView):  
   ...  
  
   def get_queryset(self):  
      # Add custom filtering logic here, e.g., filter by author  
      return Book.objects.filter(author=self.request.user)

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookCreateView(generics.CreateAPIView):
   ...
   permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
   ...
   permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
   ...
   permission_classes = [IsAuthenticated]

class BookListView(generics.ListAPIView):
   ...
   permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
   ...
   permission_classes = [IsAuthenticatedOrReadOnly]

from rest_framework.filters import DjangoFilterBackend

from django_filters import rest_framework as filters

class BookFilter(filters.FilterSet.filters.OrderingFilter.filters.SearchFilter):
   title = filters.CharFilter(field_name='title', lookup_expr='icontains')
   author = filters.CharFilter(field_name='author', lookup_expr='icontains')
   publication_year = filters.NumberFilter(field_name='publication_year', lookup_expr='exact')

   class Meta:
      model = Book
      fields = ['title', 'author', 'publication_year']

from rest_framework import generics  
from .models import Book  
from .serializers import BookSerializer  
from .filters import BookFilter  
  
class BookListView(generics.ListAPIView):  
   queryset = Book.objects.all()  
   serializer_class = BookSerializer  
   filter_backends = [DjangoFilterBackend]  
   filterset_class = BookFilter

from rest_framework.filters import SearchFilter

class BookListView(generics.ListAPIView):
   ...
   filter_backends = [DjangoFilterBackend, SearchFilter]
   search_fields = ['title', 'author']

class BookListView(generics.ListAPIView):  
   queryset = Book.objects.all()  
   serializer_class = BookSerializer  
   filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  
   filterset_class = BookFilter  
   search_fields = ['title', 'author']  
   ordering_fields = ['title', 'publication_year']

