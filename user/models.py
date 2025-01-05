from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Extending the User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username