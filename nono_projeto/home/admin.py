from django.contrib import admin
from .models import Produto

class ListProduct(admin.ModelAdmin):
  list_display = ('product_name', 'price', 'product_image', 'description')

admin.site.register(Produto, ListProduct)