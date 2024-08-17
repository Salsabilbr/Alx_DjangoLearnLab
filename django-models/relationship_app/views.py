from django.shortcuts import render
from.models import Book  
  
def list_books(request):  
   books = Book.objects.all()  
   return render(request, 'list_books.html', {'books': books})
from django.views.generic import ListView
from.models import Library

class LibraryDetailView(ListView):
   model = Library
   template_name = 'library_detail.html'
   context_object_name = 'library'
