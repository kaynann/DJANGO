from rest_framework import serializers
from cad_unico.models import Beneficiaries

class BeneficiariesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Beneficiaries
    fields = [
      'name',
      'cpf',
      'birth_date',
      'adress',
      'cep',
      'donor',
      'register_date',
    ]