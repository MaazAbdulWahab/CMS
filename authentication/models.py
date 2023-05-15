from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token as BaseToken
import uuid

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

"""
class Author(models.Model):
    user = models.OneToOneField(User, related_name="author", on_delete=models.CASCADE)
    activationStatus = models.CharField(
        max_length=10, null=False, blank=False, choices=STATUS, default=PENDING
    )
"""


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isAdmin = models.BooleanField(default=False)
    isReader = models.BooleanField(default=False)
    isWriter = models.BooleanField(default=False)
    activationStatus = models.CharField(
        max_length=10, null=True, blank=True, choices=STATUS, default=None
    )


class Token(BaseToken):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="auth_token",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )


# Create your models here.
