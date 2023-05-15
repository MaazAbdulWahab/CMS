from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.utils import CustomTokenAuth, IsAdminAllowed
from authentication.models import User, PENDING, ACTIVE, REJECTED,WITHHELD
from rest_framework.response import Response
import uuid
from rest_framework import status


# Create your views here.




class UpdateAuthorStatus(APIView):
    permission_classes=(IsAuthenticated & IsAdminAllowed)
    authentication_classes=(CustomTokenAuth)
    def put(self, request, *args,**kwargs):
        
        try:
            uu= uuid.UUID(kwargs['id'])
        except Exception as e:
            return Response({"message":"Invalid ID"}, status=status.HTTP_400_BAD_REQUESTs)
        try:
            author= User.objects.get(id=uu, isWriter=True)
        except KeyError:
            return Response({"message":"The ID field is missing"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message":"The author not found"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message":e},status=status.HTTP_400_BAD_REQUEST)
        
        status= request.data['status']

        if status == ACTIVE:
            if author.activationStatus in [PENDING,WITHHELD]:
                author.activationStatus= status
                author.save()
                

        if status == REJECTED:
            if author.activationStatus in [ACTIVE,PENDING,WITHHELD]:
                author.activationStatus= status
                author.save()

        if status == WITHHELD:
            if author.activationStatus in [ACTIVE, REJECTED]:
                author.activationStatus= status
                author.save()

        
        return Response({"message":"Updation Not Allowed"}, status=status.HTTP_400_BAD_REQUEST)