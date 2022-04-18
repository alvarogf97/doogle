from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.postgres import fields as postgres_fields
from localized_fields.fields import LocalizedTextField, LocalizedCharField
from localized_fields.util import get_language_codes


class Tag(models.Model):
    """Tag model object"""
    name = LocalizedCharField(
        null=True, blank=True, required=False,
        db_index=True, uniqueness=[*get_language_codes()])


class Breed(PolymorphicModel):
    """Breed model object"""
    name = LocalizedCharField(
        null=True, blank=True, required=False,
        db_index=True, uniqueness=[*get_language_codes()])

    weight = postgres_fields.IntegerRangeField(null=True, blank=True)
    life_span = postgres_fields.IntegerRangeField(null=True, blank=True)
    origins = models.ManyToManyField('places.Country')
    tags = models.ManyToManyField(Tag, related_name='breeds')

    def __str__(self):
        return str(self.name)


class DogBreed(Breed):
    """Dog breed model object"""
    height = postgres_fields.IntegerRangeField(null=True, blank=True)


class CatBreed(Breed):
    """Cat breed model object"""
    dog_friendly = models.PositiveSmallIntegerField(null=True, blank=True)
    child_friendly = models.PositiveSmallIntegerField(null=True, blank=True)
    

class Animal(PolymorphicModel):
    """Animal model object"""

    class Sex(models.TextChoices):
        M = 'M', 'Male'
        F = 'F', 'Female'

    name = models.CharField(max_length=255)
    sex = models.CharField(choices=Sex.choices, max_length=1, db_index=True)
    birthdate = models.DateField(null=True, blank=True)
    description = LocalizedTextField(blank=True, null=True, required=False)
    shelter = models.ForeignKey(
        'shelters.Shelter', null=True, blank=True, on_delete=models.CASCADE)
    breeds = models.ManyToManyField(Breed, related_name='animals')

    def __str__(self):
        return self.name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Photo(models.Model):
    """Animal photo model object"""
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    animal = models.ForeignKey(Animal, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.url
