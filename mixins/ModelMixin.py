from django.db import models


class SoftDelete(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CreatedAt(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAt(models.Model):
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
