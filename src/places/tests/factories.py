import factory
from places import models


class CurrencyFactory(factory.django.DjangoModelFactory):
    code = 'EUR'
    name = 'Euro'
    numeric = 978
    symbol = '€'

    class Meta:
        model = models.Currency
        django_get_or_create = ('code',)


class CountryFactory(factory.django.DjangoModelFactory):
    alpha2 = 'ES'
    alpha3 = 'ESP'
    numeric = 724
    phone_prefix = '34'
    name = 'Spain'
    locale = 'es_es'
    currency = factory.SubFactory(CurrencyFactory)

    class Meta:
        model = models.Country
        django_get_or_create = ('alpha2',)


class RegionFactory(factory.django.DjangoModelFactory):

    code = 1
    name = 'Andalucia'
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = models.Region
        django_get_or_create = ('code',)


class ProvinceFactory(factory.django.DjangoModelFactory):

    code = "11"
    name = 'Cadiz'
    region = factory.SubFactory(RegionFactory)

    class Meta:
        model = models.Province
        django_get_or_create = ('code',)


class CityFactory(factory.django.DjangoModelFactory):

    code = 21
    name = 'Jimena de la frontera'
    province = factory.SubFactory(ProvinceFactory)

    class Meta:
        model = models.City
        django_get_or_create = ('code',)
