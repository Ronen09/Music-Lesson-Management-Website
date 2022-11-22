from django.db import models
from django.contrib.auth.models import AbstractUser

from lessons.models import UserManager


class User(AbstractUser):
    email = models.EmailField("Email Address", unique=True)
    USERNAME_FIELD = "email"

    username = None

    role = models.CharField(default="Student", max_length=255)

    REQUIRED_FIELDS = []

    objects = UserManager()
