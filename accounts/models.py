from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,
                                        UserManager)
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length = 40)
    phone_number= models.CharField(max_length = 40)
    area = models.CharField(max_length = 40)
    is_active = models.BooleanField(default=True)
    is_staff= models.BooleanField(default=True)
    date_joined =models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'phone_number', 'area']

    def __str__(self):
        return '%s' % self.name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name