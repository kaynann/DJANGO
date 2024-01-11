from django.contrib import admin
from .models import Produto

class ListProduct(admin.ModelAdmin):
  list_display =('name_product', 'description', 'category', 'price')

admin.site.register(Produto, ListProduct)