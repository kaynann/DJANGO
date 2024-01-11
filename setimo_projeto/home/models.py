from django.db import models

class Produto(models.Model):
  name_product = models.CharField(max_length=100)
  description = models.TextField(max_length=350)
  category = models.CharField(max_length=60)
  price = models.FloatField(default=0.0)

  def __str__(self):
    return self.name_product
  