from django.contrib import admin
from .models import Book 
class BookAdmin(admin.ModelAdmin):
list-display = ('author', 'title', 'pub-year')  
list_filter = ('author', 'publication_year')
search_fields = ('title', 'author')
admin.site.register(Book, BookAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import CustomUser

class CustomUserAdmin(UserAdmin):
   fieldsets = (
      (None, {'fields': ('username', 'password')}),
      (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
   )
   list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
   list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
   search_fields = ('username', 'first_name', 'last_name', 'email')
   ordering = ('username',)
 admin.site.register(CustomUser, CustomUserAdmin)
