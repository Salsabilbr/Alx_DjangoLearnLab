from django.shortcuts import render
from.models import Book  
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm  
def list_books(request):  
   books = Book.objects.all()  
    ("relationship_app/list_books.html")
   return render(request, 'list_books.html', {'books': books})
from django.views.generic import ListView
from.models import Library

class LibraryDetailView(ListView):
   ("relationship_app/library_detail.html", "from .models import Library")
   ("from django.views.generic.detail import DetailView")
   model = Library
   template_name = 'library_detail.html'
   context_object_name = 'library'
from django.contrib.auth import views as auth_views  
from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm  
  
def register(request):  
   if request.method == 'POST':  
      form = UserCreationForm(request.POST)  
      if form.is_valid():  
        form.save()  
        return redirect('login')  
   else:  
      form = UserCreationForm()  
   return render(request, 'egister.html', {'form': form})  
  
def logout_view(request):  
   auth_views.logout(request)  
   return render(request, 'logout.html')
