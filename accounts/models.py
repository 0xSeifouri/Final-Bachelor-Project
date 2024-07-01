from django.db import models

from django.contrib.auth.models import AbstractUser # Need import for inheritance

class CustomUser(AbstractUser):
    pass
