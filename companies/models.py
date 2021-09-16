from django.db import models
from django_countries.fields import CountryField

from mixins.ModelMixin import CreatedAt, UpdatedAt, SoftDelete


class Companies(CreatedAt, UpdatedAt, SoftDelete):
    """Model of available companies"""

    name = models.CharField(max_length=255, verbose_name="Company name")
    location = CountryField(verbose_name="Location country")
    numOffices = models.PositiveIntegerField(verbose_name="Number of offices", default=1)
    connection = models.ManyToManyField("self", blank=True)
    personal = models.ManyToManyField('person.Person', blank=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}, {self.location}"





