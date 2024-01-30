from rest_framework import viewsets
from .serializers import MovieSerializer
from cat_filmes.models import Movie

class MovieViewSet(viewsets.ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer