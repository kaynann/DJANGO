from rest_framework import viewsets
from .serializers import BeneficiariesSerializer
from cad_unico.models import Beneficiaries

class BeneficiaresViewSet(viewsets.ModelViewSet):
  queryset = Beneficiaries.objects.all()
  serializer_class = BeneficiariesSerializer