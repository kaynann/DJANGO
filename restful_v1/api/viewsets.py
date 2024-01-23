from rest_framework import viewsets
from banco_de_sangue.models import Donors
from .serializers import DonorsSerializer

class DonorsViewSet(viewsets.ModelViewSet):
  queryset = Donors.objects.all()
  serializer_class = DonorsSerializer