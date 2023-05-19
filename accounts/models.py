from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, User


class UserA(User, PermissionsMixin):

    def __str__(self):
        return '@{}'.format(self.username)

