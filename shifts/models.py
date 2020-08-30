import datetime
from django.db import models
from trackel.supervisors.models import Supervisor

# Create your models here.
class Shift(models.Model):
    """Django data model Shifts"""

    shift_name = models.CharField(blank=True, max_length=100, verbose_name='Shift Name')
    shift_supervisor = models.OneToOneField(Supervisor, on_delete=models.CASCADE, related_name='shift', verbose_name='Shift Supervisor')
    timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now)

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'

    def __str__(self):
        code = str(self.shift_name) + " | " + str(self.shift_supervisor)
        return code
