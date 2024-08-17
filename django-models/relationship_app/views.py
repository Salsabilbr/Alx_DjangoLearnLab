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
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def check_Admin(user):
   return user.userprofile.role == 'Admin'

def check_Librarian(user):
   return user.userprofile.role == 'Librarian'

def check_Member(user):
   return user.userprofile.role == 'Member'

@admin_view = user_passes_test(check_admin)
def Admin_view(request):
   return render(request, 'Admin_view.html')

@user_passes_test(check_librarian)
def Librarian_view(request):
   return render(request, 'Librarian_view.html')

@user_passes_test(check_member)
def Member_view(request):
   return render(request, 'Member_view.html')

from django.contrib.auth.decorators import permission_required  
from django.shortcuts import render, redirect  
from.models import Book  
from.forms import BookForm  
  
@permission_required('relationship_app.can_add_book')  
def add_book(request):  
   if request.method == 'POST':  
      form = BookForm(request.POST)  
      if form.is_valid():  
        form.save()
return redirect('book_list')  
   else:  
      form = BookForm()  
   return render(request, 'add_book.html', {'form': form})  
  
@permission_required('relationship_app.can_change_book')  
def edit_book(request, pk):  
   book = Book.objects.get(pk=pk)  
   if request.method == 'POST':  
      form = BookForm(request.POST, instance=book)  
      if form.is_valid():  
        form.save()  
        return redirect('book_list')  
   else:  
      form = BookForm(instance=book)  
   return render(request, 'edit_book.html', {'form': form})  
  
@permission_required('relationship_app.can_delete_book')  
def delete_book(request, pk):  
   book = Book.objects.get(pk=pk)  
   book.delete()  
   return redirect('book_list')
