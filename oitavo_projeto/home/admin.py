from django.contrib import admin
from .models import Livro

class ListBooks(admin.ModelAdmin):
  list_display = ('book_name', 'year_of_publication', 'number_pages', 'author_name', 'publishing_company', 'price')

admin.site.register(Livro, ListBooks)
