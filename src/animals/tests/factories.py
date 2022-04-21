import factory
from animals import models
from datetime import date, timedelta
from factory import fuzzy
from localized_fields.util import get_language_codes
from shelters.tests import factories as shelter_factories


start_date = date.today() - timedelta(days=5000)


class TagFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('name')

    class Meta:
        model = models.DogBreed
        django_get_or_create = ('name',)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        name = {}
        for lang in get_language_codes():
            name[lang] = kwargs['name']
        kwargs['name'] = name
        return manager.update_or_create(*args, **kwargs)


class DogBreedFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('name')
    class Meta:
        model = models.DogBreed
        django_get_or_create = ('name',)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        name = {}
        for lang in get_language_codes():
            name[lang] = kwargs['name']
        kwargs['name'] = name
        return manager.update_or_create(*args, **kwargs)


class CatBreedFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('name')
    class Meta:
        model = models.CatBreed
        django_get_or_create = ('name',)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        name = {}
        for lang in get_language_codes():
            name[lang] = kwargs['name']
        kwargs['name'] = name
        return manager.update_or_create(*args, **kwargs)


class DogFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('name')
    sex = fuzzy.FuzzyChoice(models.Animal.Sex.choices).fuzz()[0]
    birthdate = fuzzy.FuzzyDate(start_date)
    shelter = factory.SubFactory(shelter_factories.ShelterFactory)
    
    @factory.post_generation
    def breeds(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for breed in extracted:
                self.breeds.add(breed)
        else:
            breed, _ = DogBreedFactory()
            self.breeds.add(breed)
    
    class Meta:
        model = models.Dog


class CatFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('name')
    sex = fuzzy.FuzzyChoice(models.Animal.Sex.choices)
    birthdate = fuzzy.FuzzyDate(start_date)
    shelter = factory.SubFactory(shelter_factories.ShelterFactory)

    @factory.post_generation
    def breeds(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for breed in extracted:
                self.breeds.add(breed)
        else:
            breed, _ = CatBreedFactory()
            self.breeds.add(breed)

    class Meta:
        model = models.Cat
