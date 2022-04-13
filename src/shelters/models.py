"""
Shelter models contains all related to the refuges
"""


from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Shelter(models.Model):
    """Shelter model object"""

    name = models.CharField(max_length=255, db_index=True, unique=True)
    city = models.ForeignKey('places.City', null=True, blank=True, on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'shelters'

    def __str__(self):
        return f'{self.name} ({self.city})'
