import datetime
from django.db import models
from trackel.shifts.models import Shift
from trackel.products.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

class ExtractLossData(models.Model):
    """data model for extract loss and shift"""
    month = models.IntegerField(blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=datetime.date.today, verbose_name='Week End Date')
    bbt_volume = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="BBT Volume", help_text="Enter the BBT volume.")
    packaged = models.IntegerField(blank=True, null=True, verbose_name='Packaged', help_text="Enter the volume packaged.")
    extract_loss_packaging = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='EL PKG', blank=True, null=True)

    class Meta:
        verbose_name = 'ExtractLossData'
        verbose_name_plural = 'ExtractLossData'
        ordering = ['-date']

    def __str__(self):
        return "EL-" + str(self.id) + " | W" + str(self.week) + " | " + str(self.date)

    def __unicode__(self):
        pass

@receiver(pre_save, sender=ExtractLossData)
def set_week(sender, instance, **kwargs):
    instance.week = instance.date.isocalendar()[1]
    instance.month = instance.date.month
