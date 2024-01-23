from rest_framework import serializers
from banco_de_sangue.models import Donors

class DonorsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Donors
    fields = [
      'name',
      'surname',
      'blood_type',
      'donor',
    ]