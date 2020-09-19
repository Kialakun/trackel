import datetime
from django.db import models

# Create your models here.
class Target(models.Model):
    """Django data model target"""
    name = models.CharField(blank=True, max_length=100, help_text="Give a descriptive name.")
    value = models.DecimalField(max_digits=6, decimal_places=2, help_text="Give a target value.")
    description = models.TextField(blank=True, help_text="Enter a descrpition for this target.")
    timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now)

    class Meta:
        verbose_name = 'target'
        verbose_name_plural = 'targets'

    def __str__(self):
        return str(self.name)
