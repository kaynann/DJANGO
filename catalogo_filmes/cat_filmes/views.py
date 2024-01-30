from django.shortcuts import render
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def index(request):
  movies = Movie.objects.all()
  return render(request, 'cat_filmes/index.html', {'movies': movies})

def register(request):
  if request.method == 'POST':
    form = MovieForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, 'Cadastro realizado')
      form = MovieForm()
    else:
      messages.error(request, 'Erro ao cadastrar')
  else:
    form = MovieForm()
  return render(request, 'cat_filmes/register.html',{'form': form})