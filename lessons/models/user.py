from django.db import models
from django.contrib.auth.models import AbstractUser

from lessons.models import UserManager


class User(AbstractUser):
    email = models.EmailField("Email Address", unique=True)
    USERNAME_FIELD = "email"

    username = None

    is_student = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    objects = UserManager()
