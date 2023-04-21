from rest_framework import serializers
from authentication.models import *


class CreationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password= serializers.CharField(max_length=16, min_length=8)
    firstName=serializers.CharField(min_length=8, max_length=16)
    
    lastName=serializers.CharField(min_length=8, max_length=16)

    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], first_name=validated_data['firstName'],
        last_name=validated_data['lastName'], isReader=True)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserCreationSerializer(CreationSerializer):
    pass

class AuthorCreationSerializer(CreationSerializer):
    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], first_name=validated_data['firstName'],
        last_name=validated_data['lastName'], isWriter=True, activationStatus=PENDING)
        user.set_password(validated_data['password'])
        user.save()
        return user

class AdminCreationSerializer(CreationSerializer):
    def create(self, validated_data):
        user=User.objects.create(email=validated_data['email'], first_name=validated_data['firstName'],
        last_name=validated_data['lastName'], isAdmin=True)
        user.set_password(validated_data['password'])
        user.save()
        return user
