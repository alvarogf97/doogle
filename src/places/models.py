"""
Places models have the information about the organizaion
of a territory, linked with his concrete place and useful
for addresses respresentation
"""


from django.db import models


class Currency(models.Model):
    """Currency model object"""
    code = models.CharField(
        max_length=3, db_index=True, unique=True, help_text='ISO 4217')
    numeric = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'currencies'


class Country(models.Model):
    """Country model object"""
    alpha2 = models.CharField(max_length=2, db_index=True, unique=True)
    alpha3 = models.CharField(max_length=3, db_index=True, unique=True)
    numeric = models.CharField(max_length=3, unique=True)
    phone_prefix = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    official_name = models.CharField(max_length=128, blank=True)
    continent = models.CharField(max_length=2)
    capital = models.CharField(max_length=255)
    locale = models.CharField(max_length=8)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.CASCADE)
    currency_name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'


class Region(models.Model):
    """Region model object"""
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    code = models.PositiveIntegerField(db_index=True)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = (('country', 'code'),)

    def __str__(self):
        return self.name


class Province(models.Model):
    """Province model object"""
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    code = models.CharField(max_length=2, db_index=True)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = (('region', 'code'),)

    def __str__(self):
        return self.name


class City(models.Model):
    """City model object"""
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    code = models.PositiveIntegerField(db_index=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = (('province', 'code'),)
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name
