from django.contrib import admin
from shelters import models


@admin.register(models.Shelter)
class ShelterAdmin(admin.ModelAdmin):
    pass
