from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Resort


class ResortSerializer(serializers.ModelSerializer):
    """Create serialized Resort objects to serve from the API."""
    class Meta:
        model = Resort
        #TODO: Add additional Resort fields as needed
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    #TODO: build UserSerializer class
    pass


class TeamSerializer(serializers.ModelSerializer):
    #TODO: build TeamSerializer class
    pass


class MessageSerializer(serializers.ModelSerializer):
    #TODO: build MessageSerializer class
    pass
