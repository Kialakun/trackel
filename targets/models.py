from django.db import models

# Create your models here.
class target(models.Model):
    """Django data model target"""
    name = models.CharField(blank=True, max_length=100)
    value = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'target'
        verbose_name_plural = 'targets'

    def __str__(self):
        return str(self.id)
