from django.contrib.auth.models import AbstractUser
from django.db import models


class MyCustomUser(AbstractUser):
    points = models.IntegerField(
        default=0
    )

