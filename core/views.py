from django.shortcuts import render
from rest_framework.views import APIView
from authentication.utils import CustomTokenAuth
from rest_framework.permissions import IsAuthenticated
from core.models import Keywords
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class KeywordCrud(APIView):
    authentication_classes= (CustomTokenAuth)
    permission_classes=(IsAuthenticated)

    def get(self,request,*args,**kwargs):
        word=request.GET.get('word')
        presentWords=Keywords.objects.filter(word__icontains=word).values_list('word')
        return Response(presentWords, status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        word= request.data['word']
        if type(word) == list:

            Keywords.objects.bulk_create(list(map(lambda x :Keywords(word=x),word)))
        
        else:
            Keywords.objects.create(word=word)
        return Response({"message":"Created"},status=status.HTTP_201_CREATED)




