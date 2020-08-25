from django.db import models

# Create your models here.
class Products(models.Model):
    """Django data model Products"""
    PACKETS = (('24s', '24s'), ('4x6s', '4x6s'))
    product_name = models.CharField(blank=True, max_length=100)
    product_packaging = models.CharField(blank=True, max_length=100, choices=PACKETS)
    product_code = models.CharField(blank=True, max_length=8, null=True)

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

    def __str__(self):
        code = str(self.product_name) + " | " + str(self.product_packaging)
        return code
