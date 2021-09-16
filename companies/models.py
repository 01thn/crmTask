from django.db import models
from django_countries.fields import CountryField


class Companies(models.Model):
    name = models.CharField(max_length=255, verbose_name="Company name")
    is_active = models.BooleanField(default=True)
    location = CountryField(verbose_name="Location country")
    numOffices = models.PositiveIntegerField(verbose_name="Number of offices", default=1)
    connection = models.ManyToManyField("self", blank=True)
    personal = models.ManyToManyField('person.Person', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}, {self.location}"





