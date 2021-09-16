from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserModel(AbstractBaseUser):
    """Model for creation user"""

    login = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, verbose_name="e-mail", unique=True)
    admin = models.BooleanField(default=False)