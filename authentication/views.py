from authentication.models import CustomToken
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import *

# Create your views here.
from rest_framework.views import APIView


class Login(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "Email Incorrect"}, status=HTTP_404_NOT_FOUND)

        if not user.check_password(request.data.get("password")):
            return Response({"message": "Wrong Password"}, status=HTTP_400_BAD_REQUEST)

        token = CustomToken.objects.create(user=user)

        return Response({"message": "Success", "token": token.key}, status=HTTP_200_OK)
