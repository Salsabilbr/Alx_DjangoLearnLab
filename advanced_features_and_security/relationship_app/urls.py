from django.urls import path  
from. import views  
from .views import list_books  
urlpatterns = [  
   path('books/', views.list_books, name='list_books'),  
   path('library/<pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
   path("views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=")
from django.urls import path  
from. import views  
from django.contrib.auth import views as auth_views  
  
urlpatterns = [  
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  
   path('logout/', views.logout_view, name='logout'),  
   path('register/', views.register, name='register'),
   path('Admin/', views.admin_view, name='Admin_view'),
   path('Librarian/', views.librarian_view, name='Librarian_view'),
   path('Member/', views.member_view, name='Member_view'),
]] 

from django.urls import path  
from. import views  
  
urlpatterns = [  
   path('admin/', views.admin_view, name='admin_view'),  
   path('librarian/', views.librarian_view, name='librarian_view'),  
   path('member/', views.member_view, name='member_view'),  
]

from django.urls import path
from. import views

urlpatterns = [
   path('add_book/', views.add_book, name='add_book'),
   path('edit_book/<pk>/', views.edit_book, name='edit_book'),
   path('delete_book/<pk>/', views.delete_book, name='delete_book'),
]
