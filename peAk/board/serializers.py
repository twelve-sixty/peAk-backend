from rest_framework import serializers
# from django.contrib.auth.models import PeakUser
from .models import Resort, PeakUser, Team


class ResortSerializer(serializers.ModelSerializer):
    """Create serialized Resort objects to serve from the API."""
    name = serializers.ReadOnlyField(source='resort_name')
    latitude = serializers.ReadOnlyField(source='resort_location_latitude')
    longitude = serializers.ReadOnlyField(source='resort_location_longitude')
    websiteUrl = serializers.ReadOnlyField(source='resort_website_url')
    altitude = serializers.ReadOnlyField(source='resort_altitude')
    #TODO: Map address fields into address: {..} per spec provided by JAVA team
    class Meta:
        model = Resort

        fields = ('id', 'name', 'latitude', 'longitude', 'resort_address_line1',
                  'resort_address_line2', 'resort_address_city', 'resort_address_state', 'resort_address_zip_code',
                  'websiteUrl', 'altitude')

class UserSerializer(serializers.ModelSerializer):
    #TODO: build UserSerializer class
    password = serializers.CharField(write_only=True)
    email = serializers.Field(source='user_email')

    class Meta:
        model = PeakUser
        fields = (
            'id',
            'username',
            'email',
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
    name = serializers.ReadOnlyField(source='team_name')
    description = serializers.ReadOnlyField(source='team_description')
    #TODO: Add a currentCapacity that updates whenever a user is added to a team
    currentCapacity = serializers.ReadOnlyField(source='team_max_capacity')
    maxCapacity = serializers.ReadOnlyField(source='team_max_capacity')
    meetDate = serializers.ReadOnlyField(source='team_meet_date')
    #TODO: resort is not serializable. How do we represent that?
    # resort = serializers.ReadOnlyField(source='team_resort')
    status = serializers.ReadOnlyField(source='team_status')

    class Meta:
        model = Team
        fields = ('id', 'name', 'description', 'currentCapacity', 'maxCapacity', 'meetDate', 'status')


class MessageSerializer(serializers.ModelSerializer):
    #TODO: build MessageSerializer class
    pass
