import factory
from shelters import models
from places.tests import factories as places_factories


class ShelterFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('company')
    city = factory.SubFactory(places_factories.CityFactory)
    url = factory.Faker('url')
    mail = factory.Faker('email')

    class Meta:
        model = models.Shelter
