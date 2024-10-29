from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email
