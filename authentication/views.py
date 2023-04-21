from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import *

# Create your views here.
from rest_framework.views import APIView

from authentication.models import Token, User
from authentication.utils import CustomTokenAuth
from authentication.serializers import UserCreationSerializer, AuthorCreationSerializer, AdminCreationSerializer


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

        token = Token.objects.create(user=user)

        return Response({"message": "Success", "token": token.key}, status=HTTP_200_OK)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CustomTokenAuth,)

    def post(self, request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        auth_header = auth_header.split(" ")[1]
        Token.objects.get(key=auth_header).delete()
        return Response({"message": "Success"}, status=HTTP_200_OK)


class UserSignup(APIView):
    permission_classes=()
    authentication_classes=()
    serializer_class= UserCreationSerializer
    def post(self, request,*args,**kwargs):
        
        ser= self.ser_class(request.data)

        if ser.is_valid():
            ser.save()
            return Response({"message":"Created"}, status= HTTP_200_OK)

        else:
            return Response({"message":ser.error_messages}, status=HTTP_400_BAD_REQUEST)


class AuthorSignup(UserSignup):
   serializer_class= AuthorCreationSerializer


class AdminSignup(APIView):
   serializer_class= AdminCreationSerializer



class ChangePassword(APIView):
    permission_classes= (IsAuthenticated)
    authentication_classes=(CustomTokenAuth)
    
    def post(self,request,*args,**kwargs):
        
        user=request.user

        if user.check_password(request.data['oldPassword']):
            user.set_password(request.data['newPassword'])
            user.save()
            Token.objects.filter(user=user).delete()
            return Response({"message":"Password Changed"}, status= HTTP_200_OK)
        
        else:
            return Response({"message":"Wrong Password"}, status=HTTP_400_BAD_REQUEST)
