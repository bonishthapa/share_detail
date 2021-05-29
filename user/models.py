from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.IntegerField(null=True,blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    # is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email