from django.contrib import admin
from .models import Book 
class BookAdmin(admin.ModelAdmin):
list-display = ('author', 'title', 'pub-year')  
list_filter = ('author', 'publication_year')
search_fields = ('title', 'author')
admin.site.register(Book, BookAdmin)
