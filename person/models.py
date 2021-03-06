from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from skills.models import Skills

from mixins.ModelMixin import CreatedAt, UpdatedAt, SoftDelete


class Person(CreatedAt, UpdatedAt, SoftDelete):
    """Model of available persons"""

    lastName = models.CharField(max_length=30, verbose_name="Last name")
    firstName = models.CharField(max_length=30, verbose_name="First name")
    patronymic = models.CharField(max_length=30, verbose_name="Patronymic")
    age = models.PositiveIntegerField(verbose_name="Age", default=18, validators=[
            MaxValueValidator(100),
            MinValueValidator(18)
        ], help_text="Person must be older than 18 years old")
    education = models.CharField(max_length=255, verbose_name="Education")
    company = models.ManyToManyField("companies.Companies", blank=True)
    position = models.CharField(max_length=30, verbose_name="Position")
    skills = models.ManyToManyField(Skills, blank=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return f"{self.firstName} {self.lastName}, {self.age}"
