from rest_framework import serializers
from authentication.models import *
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator


class CreationSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all().values('email'))])
    password= serializers.CharField(max_length=16, min_length=8)
    first_name=serializers.CharField(min_length=4, max_length=16)
    
    last_name=serializers.CharField(min_length=4, max_length=16)

    class Meta:
       
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all().values('first_name','last_name'),
                fields=['first_name', 'last_name']
            )
        ]


class UserCreationSerializer(CreationSerializer):

    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],
        last_name=validated_data['last_name'], isReader=True, username=validated_data['first_name']+validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    


class AuthorCreationSerializer(CreationSerializer):

    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],
        last_name=validated_data['last_name'], isWriter=True, activationStatus=PENDING,
        username=validated_data['first_name']+validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
 

class AdminCreationSerializer(CreationSerializer):

    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],
        last_name=validated_data['last_name'], isAdmin=True,username=validated_data['first_name']+validated_data['last_name'],
        activationStatus=PENDING)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
