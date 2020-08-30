import datetime
from django.db import models
from trackel.shifts.models import Shift
from trackel.products.models import Product

# Create your models here.
class ExtractLossData(models.Model):
    """data model for extract loss and shift"""

    SHIFT_TYPE = (
        ("DAY", "Day Shift"),
        ("NIGHT", "Night Shift")
    )

    BBT = (
        (1,'BBT# 1'),
        (2,'BBT# 2'),
        (3,'BBT# 3'),
        (4,'BBT# 4'),
        (5,'BBT# 5'),
        (6,'BBT# 6'),
        (7,'BBT# 7'),
        (8,'BBT# 8'),
        (9,'BBT# 9'),
        (10,'BBT# 10')
    )

    LINES = (('can', 'Can Line'), ('bottle', 'Bottle Line'))

    week = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=datetime.date.today, verbose_name='Date')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='shift_extract_loss_data', verbose_name='Shift')
    shift_type = models.CharField(blank=True, max_length=100, choices=SHIFT_TYPE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_extract_loss', verbose_name='Product')
    line = models.CharField(blank=True, max_length=100, choices=LINES, verbose_name='Line')
    og = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='OG')
    bbt_number = models.IntegerField(blank=True, null=True, choices=BBT, verbose_name='BBT#')
    bbt_volume = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="BBT Volume", help_text="Enter the BBT volume.")
    packaged = models.IntegerField(blank=True, null=True, verbose_name='Packaged', help_text="Enter the volume packaged.")
    fill_content = models.IntegerField(blank=True, null=True, verbose_name='Fill Content')
    extract_loss_packaging = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='EL PKG', blank=True, null=True)

    class Meta:
        verbose_name = 'ExtractLossData'
        verbose_name_plural = 'ExtractLossData'
        ordering = ['-date']

    def __str__(self):
        return "W" + str(self.week) + " | " + str(self.date) + " | " + str(self.shift)

    def __unicode__(self):
        pass
