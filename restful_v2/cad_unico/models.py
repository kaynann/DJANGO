from django.db import models

class Beneficiaries(models.Model):
  name =  models.CharField(max_length=120, blank=True, null=True)
  cpf = models.CharField(max_length=14, blank=False, null=False)
  birth_date = models.DateField(blank=True, null=True)
  adress = models.CharField(max_length=150)
  cep = models.CharField(max_length=10, blank=True, null=True)
  donor = models.BooleanField(default=False)
  register_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name