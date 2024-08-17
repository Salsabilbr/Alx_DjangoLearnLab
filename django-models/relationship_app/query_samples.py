from django.db.models import F
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name='John Doe')
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

# List all books in a library
library = Library.objects.get(name='New York Public Library')
books_in_library = library.books.all()
print(books_in_library)

# Retrieve the librarian for a library
library = Library.objects.get(name='New York Public Library')
librarian = Librarian.objects.get(library=library)
Library.objects.get(name=library_name)
print(librarian.name)
