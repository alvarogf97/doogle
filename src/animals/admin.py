from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from animals import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class BaseAnimalAdmin(PolymorphicChildModelAdmin):
    base_model = models.Animal


class BaseBreedAdmin(PolymorphicChildModelAdmin):
    base_model = models.Breed


@admin.register(models.Animal)
class AnimalAdmin(PolymorphicParentModelAdmin):
    base_model = models.Animal
    child_models = (models.Dog, models.Cat)
    list_filter = (PolymorphicChildModelFilter,)


@admin.register(models.Dog)
class DogAdmin(BaseAnimalAdmin):
    base_model = models.Dog


@admin.register(models.Cat)
class CatAdmin(BaseAnimalAdmin):
    base_model = models.Cat


@admin.register(models.Breed)
class BreedAdmin(PolymorphicParentModelAdmin):
    base_model = models.Breed
    child_models = (models.DogBreed, models.CatBreed)
    list_filter = (PolymorphicChildModelFilter,)


@admin.register(models.DogBreed)
class DogBreedAdmin(BaseBreedAdmin):
    base_model = models.DogBreed


@admin.register(models.CatBreed)
class CatBreedAdmin(BaseBreedAdmin):
    base_model = models.CatBreed


@admin.register(models.Photo)
class Photo(admin.ModelAdmin):
    pass
