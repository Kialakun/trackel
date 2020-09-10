import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from trackel.el.models import ExtractLossData
from trackel.products.models import Product
# Create your models here.
class Heuft1(models.Model):
    """Django data model Heuft1"""

    LINES = (('CAN', 'Can Line'), ('BOTTLE', 'Bottle Line'))

    date = models.DateField(default=datetime.datetime.today)
    line = models.CharField(blank=True, max_length=100, choices=LINES, verbose_name='Line')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='heuft_1_product', verbose_name='Product')
    fill_content = models.IntegerField(blank=True, null=True, verbose_name='Fill Content')

    filling_tube = models.DecimalField(max_digits=6, decimal_places=2)
    filling = models.DecimalField(max_digits=6, decimal_places=2)
    closure = models.DecimalField(max_digits=6, decimal_places=2)
    total_loss = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Heuft1'
        verbose_name_plural = 'Heuft1s'

    def __str__(self):
        return str(self.id)

class Heuft2(models.Model):
    """Django data model LossDeployment"""

    LINES = (('CAN', 'Can Line'), ('BOTTLE', 'Bottle Line'))

    date = models.DateField(default=datetime.datetime.today)
    line = models.CharField(blank=True, max_length=100, choices=LINES, verbose_name='Line')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='heuft_2_product', verbose_name='Product')
    fill_content = models.IntegerField(blank=True, null=True, verbose_name='Fill Content')

    canted_closure = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    leaking_pressure = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    low_fill = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    uncrowned = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    total_loss = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Heuft2'
        verbose_name_plural = 'Heuft2s'

    def __str__(self):
        return str(self.id)

@receiver(pre_save, sender=Heuft2)
def save_total_loss(sender, instance, **kwargs):
    instance.total_loss = instance.canted_closure + instance.leaking_pressure + instance.low_fill + instance.uncrowned

@receiver(pre_save, sender=Heuft1)
def save_total_loss(sender, instance, **kwargs):
    instance.total_loss = instance.filling_tube + instance.filling + instance.closure
