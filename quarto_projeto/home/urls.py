from django.urls import path
from .views import meu_home

urlpatterns = [
  path('home', meu_home),
]