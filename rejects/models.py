from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from trackel.el.models import ExtractLossData
from trackel.products.models import Product
# Create your models here.

class LossDeployment(models.Model):
    """Django data model LossDeployment"""

    LINES = (('CAN', 'Can Line'), ('BOTTLE', 'Bottle Line'))
    HEUFTS = ((1, 'Heuft 1'), (2, 'Heuft 2'))

    extract_loss_record = models.ForeignKey(ExtractLossData, on_delete=models.CASCADE, related_name='loss_deployment', verbose_name='Extract Loss Record')
    line = models.CharField(blank=True, max_length=100, choices=LINES, verbose_name='Line')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_extract_loss', verbose_name='Product')
    fill_content = models.IntegerField(blank=True, null=True, verbose_name='Fill Content')
    og = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='OG')
    heuft_number = models.IntegerField(choices=HEUFTS)
    canted_closure = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    leaking_pressure = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    canted_closure = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    leaking_pressure = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    low_fill = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    uncrowned = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    total_loss = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'LossDeployment'
        verbose_name_plural = 'LossDeployments'

    def __str__(self):
        return str(self.id)

@receiver(pre_save, sender=LossDeployment)
def save_total_loss(sender, instance, **kwargs):
    instance.total_loss = instance.canted_closure + instance.leaking_pressure + instance.low_fill + instance.uncrowned
