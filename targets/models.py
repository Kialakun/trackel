import datetime
from django.db import models

# Create your models here.
class Target(models.Model):
    """Django data model target"""
    extract_loss = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Extract Loss Target')
    heuft = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Heuft Target')
    timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now)

    class Meta:
        verbose_name = 'target'
        verbose_name_plural = 'targets'

    def __str__(self):
        return str(self.id) + ' | Extract Loss: ' + str(self.extract_loss) + ' | Heuft: ' + str(self.heuft)
