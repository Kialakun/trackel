from django.db import models

# Create your models here.
class Shift(models.Model):
    """Django data model Shifts"""

    shift_name = models.CharField(blank=True, max_length=100, verbose_name='Shift Name')
    shift_supervisor = models.OneToOneField(Supervisors, on_delete=models.CASCADE, related_name='shift', verbose_name='Shift Supervisor')

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'

    def __str__(self):
        code = str(self.shift_name) + " | " + str(self.shift_supervisor)
        return code
