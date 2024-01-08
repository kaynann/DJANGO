from django.shortcuts import render
from django.http import HttpResponse

def meu_home(request):
  return HttpResponse('<h1>Meu primeiro web app</h1>')