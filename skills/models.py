from django.db import models

from mixins.ModelMixin import CreatedAt, UpdatedAt, SoftDelete


class Skills(CreatedAt, UpdatedAt, SoftDelete):
    """Model of available skills"""

    knowledge = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.knowledge}"
