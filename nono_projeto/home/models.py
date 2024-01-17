from django.db import models
from stdimage import StdImageField

class Produto(models.Model):
  product_name = models.CharField(max_length=120)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  product_image = StdImageField(upload_to='produtos', variations={'thumb': (124, 124)}, delete_orphans=True)
  description = models.TextField()

  def __str__(self):
    return self.product_name