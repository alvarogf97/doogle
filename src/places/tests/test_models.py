from django.test import TestCase
from places import models


class CurrencyTest(TestCase):

    fixtures = [
        'currencies'
    ]

    def test_currency_str(self):
        currency = models.Currency.objects.last()
        self.assertEqual(str(currency), currency.name)


class CountryTest(TestCase):

    fixtures = [
        'currencies',
        'countries'
    ]

    def test_country_str(self):
        country = models.Country.objects.last()
        self.assertEqual(str(country), country.name)


class RegionTest(TestCase):

    fixtures = [
        'currencies',
        'countries',
        'regions'
    ]

    def test_region_str(self):
        region = models.Region.objects.last()
        self.assertEqual(str(region), region.name)


class ProvinceTest(TestCase):

    fixtures = [
        'currencies',
        'countries',
        'regions',
        'provinces'
    ]

    def test_currency_str(self):
        province = models.Province.objects.last()
        self.assertEqual(str(province), province.name)


class CityTest(TestCase):

    fixtures = [
        'currencies',
        'countries',
        'regions',
        'provinces',
        'cities'
    ]

    def test_currency_str(self):
        city = models.City.objects.last()
        self.assertEqual(str(city), city.name)
