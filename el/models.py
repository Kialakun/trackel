from django.db import models

# Create your models here.
class ExtractLossData(models.Model):
    # TODO: Define fields here

    BBT = ((1,'BBT# 1'),(2,'BBT# 2'),(3,'BBT# 3'),(4,'BBT# 4'),(5,'BBT# 5'),(6,'BBT# 6'),(7,'BBT# 7'),(8,'BBT# 8'),(9,'BBT# 9'),(10,'BBT# 10'))
    LINES = (('can', 'Can Line'), ('bottle', 'Bottle Line'))

    week = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=datetime.datetime.now, verbose_name='Date')
    shift = models.ForeignKey(Shifts, on_delete=models.CASCADE, related_name='shift_extract_loss_data', verbose_name='Shift')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_extract_loss', verbose_name='Product')
    line = models.CharField(blank=True, max_length=100, choices=LINES, verbose_name='Line')
    og = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='OG')
    bmf = models.IntegerField(blank=True, null=True, verbose_name="BMF")
    bbt_number = models.IntegerField(blank=True, null=True, choices=BBT, verbose_name='BBT#')
    pkg_filler = models.IntegerField(blank=True, null=True, verbose_name='PKG Filler')
    packaged = models.IntegerField(blank=True, null=True, verbose_name='Packaged')
    fill_content = models.IntegerField(blank=True, null=True, verbose_name='Fill Content')
    heuft_1_rejects = models.IntegerField(blank=True, null=True, verbose_name='Heuft 1 Rejects')
    heuft_2_rejects = models.IntegerField(blank=True, null=True, verbose_name='Heuft 2 Rejects')
    extract_loss_packaging_line = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='EL PKG Line')
    extract_loss_packaging = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='EL PKG')

    class Meta:
        verbose_name = 'ExtractLossData'
        verbose_name_plural = 'ExtractLossData'
        ordering = ['date']

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        pass
