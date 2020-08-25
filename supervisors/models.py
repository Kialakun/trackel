from django.db import models

# Create your models here.
class Supervisors(models.Model):
    """Django data model Supervisors"""

    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = 'Supervisors'
        verbose_name_plural = 'Supervisors'

    def __str__(self):
        string_name = str(self.first_name) + ' ' + str(self.last_name)
        return string_name
