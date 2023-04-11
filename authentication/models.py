from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

ACTIVE = "ACTIVE"
PENDING = "PENDING"
REJECTED = "REJECTED"
WITHHELD = "WITHHELD"
STATUS = [
    (ACTIVE, "ACTIVE"),
    (PENDING, "PENDING"),
    (REJECTED, "REJECTED"),
    (WITHHELD, "WITHHELD"),
]


class Author(models.Model):
    user = models.OneToOneField(User, related_name="author", on_delete=models.CASCADE)
    activationStatus = models.CharField(
        max_length=10, null=False, blank=False, choices=STATUS, default=PENDING
    )


class CustomToken(Token):
    user = models.ForeignKey(User, related_name="tokens", on_delete=models.CASCADE)


# Create your models here.
