from django.db import models
from trackel.el.models import ExtractLossData

# Create your models here.
class LossDeployment(models.Model):
    """Django data model LossDeployment"""

    extract_loss_record = models.ForeignKey(ExtractLossData, on_delete=models.CASCADE, related_name='loss_deployment', verbose_name='Shift')
    heuft_1_rejects = models.DecimalField(max_digits=3, decimal_places=2,blank=True, null=True, verbose_name='Heuft 1 Rejects')
    heuft_2_rejects = models.DecimalField(max_digits=3, decimal_places=2,blank=True, null=True, verbose_name='Heuft 2 Rejects')

    class Meta:
        verbose_name = 'LossDeployment'
        verbose_name_plural = 'LossDeployments'

    def __str__(self):
        return str(self.id)
