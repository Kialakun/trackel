from django.db import models
from trackel.el.models import ExtractLossData
from trackel.products.models import Product
# Create your models here.
class LossDeployment(models.Model):
    """Django data model LossDeployment"""

    LINES = (('CAN', 'Can Line'), ('BOTTLE', 'Bottle Line'))

    extract_loss_record = models.ForeignKey(ExtractLossData, on_delete=models.CASCADE, related_name='loss_deployment', verbose_name='Shift')
    line = models.CharField(blank=True, max_length=100, choices=LINES, verbose_name='Line')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_extract_loss', verbose_name='Product')
    fill_content = models.IntegerField(blank=True, null=True, verbose_name='Fill Content')
    og = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='OG')
    heuft_1_rejects = models.DecimalField(max_digits=3, decimal_places=2,blank=True, null=True, verbose_name='Heuft 1 Rejects')
    heuft_2_rejects = models.DecimalField(max_digits=3, decimal_places=2,blank=True, null=True, verbose_name='Heuft 2 Rejects')

    class Meta:
        verbose_name = 'LossDeployment'
        verbose_name_plural = 'LossDeployments'

    def __str__(self):
        return str(self.id)
