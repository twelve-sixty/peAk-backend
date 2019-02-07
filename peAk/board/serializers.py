from rest_framework import serializers
# from django.contrib.auth.models import PeakUser
from .models import Resort, PeakUser, Team


class UserSerializer(serializers.ModelSerializer):
    """

    """
    username = serializers.ReadOnlyField(source='user_username')
    bio = serializers.ReadOnlyField(source='user_bio')
    # TODO: turn age into an actual calculation from birthdate
    age = serializers.ReadOnlyField(source='user_date_of_birth')
    favResort = serializers.ReadOnlyField(source='user_fav_resort', required=False, allow_null=True)
    teamBelong = serializers.ReadOnlyField(source='user_team_belong', required=False, allow_null=True)

    class Meta:
        model = PeakUser
        fields = (
            'id',
            'username',
            'bio',
            'age',
            'favResort',
            'teamBelong')


class TeamOverviewSerializer(serializers.ModelSerializer):
    """Serializes Team objects for inclusion in serialized Resort data. It does not
    include serialized User data."""
    name = serializers.ReadOnlyField(source='team_name')
    description = serializers.ReadOnlyField(source='team_description')
    # TODO: Add a currentCapacity that updates whenever a user is added to a
    # team
    currentCapacity = serializers.ReadOnlyField(source='team_max_capacity')
    maxCapacity = serializers.ReadOnlyField(source='team_max_capacity')
    meetDate = serializers.ReadOnlyField(source='team_meet_date')
    status = serializers.ReadOnlyField(source='team_status')

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'description',
            'currentCapacity',
            'maxCapacity',
            'meetDate',
            'status')

class TeamDetailSerializer(serializers.ModelSerializer):
    """Serializes Team objects for detailed view. This includes serialized User objects
    representing members of the Team."""
    name = serializers.ReadOnlyField(source='team_name')
    description = serializers.ReadOnlyField(source='team_description')
    # TODO: Add a currentCapacity that updates whenever a user is added to a
    # team
    currentCapacity = serializers.ReadOnlyField(source='team_max_capacity')
    maxCapacity = serializers.ReadOnlyField(source='team_max_capacity')
    meetDate = serializers.ReadOnlyField(source='team_meet_date')
    status = serializers.ReadOnlyField(source='team_status')
    users = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'description',
            'currentCapacity',
            'maxCapacity',
            'meetDate',
            'status',
            'users')


class ResortSerializer(serializers.ModelSerializer):
    """Create serialized Resort objects to serve from the API."""
    name = serializers.ReadOnlyField(source='resort_name')
    latitude = serializers.ReadOnlyField(source='resort_location_latitude')
    longitude = serializers.ReadOnlyField(source='resort_location_longitude')
    websiteUrl = serializers.ReadOnlyField(source='resort_website_url')
    altitude = serializers.ReadOnlyField(source='resort_altitude')
    # Nested serializer for including teams in resort JSON
    teams = TeamOverviewSerializer(many=True)
    # TODO: Map address fields into address: {..} per spec provided by JAVA team

    class Meta:
        model = Resort

        fields = (
            'id',
            'name',
            'latitude',
            'longitude',
            'resort_address_line1',
            'resort_address_line2',
            'resort_address_city',
            'resort_address_state',
            'resort_address_zip_code',
            'websiteUrl',
            'altitude',
            'teams',
            # 'resort_team'
        )


class MessageSerializer(serializers.ModelSerializer):
    # TODO: build MessageSerializer class
    pass
