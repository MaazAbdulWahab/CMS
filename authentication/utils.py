from datetime import timedelta

from authentication.models import CustomToken
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class CustomTokenAuth(TokenAuthentication):
    def get_model(self):
        return CustomToken

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related("user").get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid token."))
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_("User inactive or deleted."))
        if (
            token.created + timedelta(minutes=settings.TOKEN_EXPIRATION)
            < timezone.now()
        ):
            token.delete()
            raise exceptions.AuthenticationFailed(_("Token Expired"))
        return (token.user, token)
