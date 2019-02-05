from rest_framework import serializers
# from django.contrib.auth.models import PeakUser
from .models import Resort, PeakUser


class ResortSerializer(serializers.ModelSerializer):
    """Create serialized Resort objects to serve from the API."""
    class Meta:
        model = Resort
        fields = ('id', 'resort_name', 'resort_location_latitude', 'resort_location_longitude', 'resort_address_line1',
                  'resort_address_line2', 'resort_address_city', 'resort_address_state', 'resort_address_zip_code',
                  'resort_website_url', 'resort_altitude')

class UserSerializer(serializers.ModelSerializer):
    #TODO: build UserSerializer class
    password = serializers.CharField(write_only=True)
    class Meta:
        model = PeakUser
        fields = (
            'id',
            'username',
            'user_email',
            'user_name_first',
            'user_name_last',
            'user_fav_resort',
            'user_date_of_birth',
            'user_groups_belong',
            'user_profile_picture',
            'user_date_joined')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email']
        })
        user.set_password(validated_data['password'])
        user.save()
        return user

class TeamSerializer(serializers.ModelSerializer):
    #TODO: build TeamSerializer class
    pass


class MessageSerializer(serializers.ModelSerializer):
    #TODO: build MessageSerializer class
    pass
