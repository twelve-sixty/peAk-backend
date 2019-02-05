from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Resort


class ResortSerializer(serializers.ModelSerializer):
    """Create serialized Resort objects to serve from the API."""
    class Meta:
        model = Resort
        #TODO: Add additional Resort fields as needed
        fields = ('id', 'resort_name', 'resort_location_lat', 'resort_location_long', 'resort_address_line1',
                  'resort_address_line2', 'resort_address_city', 'resort_address_state', 'resort_address_zip_code',
                  'resort_website_url', 'resort_altitude')

class UserSerializer(serializers.ModelSerializer):
    #TODO: build UserSerializer class
    pass


class TeamSerializer(serializers.ModelSerializer):
    #TODO: build TeamSerializer class
    pass


class MessageSerializer(serializers.ModelSerializer):
    #TODO: build MessageSerializer class
    pass
