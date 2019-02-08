from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Resort, PeakUser, Team


class TeamOverviewSerializer(serializers.ModelSerializer):
    """Serializes Team objects for inclusion in serialized Resort data. It does not
    include serialized User data."""

    # Map field names from our db fields to the ones expected by the frontend
    name = serializers.ReadOnlyField(source='team_name')
    description = serializers.ReadOnlyField(source='team_description')
    # TODO: Add a currentCapacity that updates whenever a user is added to a team
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


class UserSerializer(serializers.ModelSerializer):
    """
    """

    # Map field names from our db fields to the ones expected by the frontend
    username = serializers.ReadOnlyField(source='user_username')
    bio = serializers.ReadOnlyField(source='user_bio')
    # TODO: turn age into an actual calculation from birthdate
    age = serializers.ReadOnlyField(source='user_date_of_birth')
    favResort = serializers.ReadOnlyField(source='user_fav_resort', required=False, allow_null=True)
    # teams = serializers.ReadOnlyField(source='user_team_belong', required=False, allow_null=True)
    teams = TeamOverviewSerializer(source='user_team_belong', many=True)

    class Meta:
        model = PeakUser
        fields = (
            'id',
            'username',
            'bio',
            'age',
            'favResort',
            'teams')


# class CreateUserSerializer(serializers.ModelSerializer):
#     """Create serialized User objects."""
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'email',
#             'password',
#             'first_name',
#             'last_name')
#
#     def create(self, validated_data):
#         print('*****', self.data)
#         user = super().create({
#             'username': validated_data['username'],
#             'email': validated_data['email'],
#             'bio': self.data['bio']
#             # 'user_firstName': validated_data['firstName'],
#             # 'user_lastName': validated_data['lastName'],
#             # 'user_date_of_birth': validated_data['birthDate']
#
#
#         })
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


class CreateUserSerializer(serializers.ModelSerializer):
    """Create serialized User objects."""
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name')

    def create(self, validated_data):
        print('*****', self.data)
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
            # 'peakuser.bio': validated_data['bio']
            # 'user_firstName': validated_data['firstName'],
            # 'user_lastName': validated_data['lastName'],
            # 'user_date_of_birth': validated_data['birthDate']


        })
        user.set_password(validated_data['password'])
        user.save()
        return user


class TeamDetailSerializer(serializers.ModelSerializer):
    """Serializes Team objects for detailed view. This includes serialized User objects
    representing members of the Team."""

    # Map field names from our db fields to the ones expected by the frontend
    name = serializers.ReadOnlyField(source='team_name')
    description = serializers.ReadOnlyField(source='team_description')
    # TODO: Add a currentCapacity that updates whenever a user is added to a team
    currentCapacity = serializers.ReadOnlyField(source='team_max_capacity')
    maxCapacity = serializers.ReadOnlyField(source='team_max_capacity')
    meetDate = serializers.ReadOnlyField(source='team_meet_date')
    status = serializers.ReadOnlyField(source='team_status')
    users = UserSerializer(many=True, default=None)

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


class TeamCreateSerializer(serializers.ModelSerializer):
    """Serializes Team objects for creation."""

    # TODO: Add a currentCapacity that updates whenever a user is added to a team

    class Meta:
        model = Team
        fields = (
            'id',
            'team_name',
            'team_description',
            'team_max_capacity',
            'team_meet_date',
            'team_status',
            'team_tags',
            'team_administrator',
            'team_resort'
        )

    def create(self, validated_data):
        print(self.data)
        # print('**validated_data**', validated_data)
        team = super().create({
            'team_name': validated_data['team_name'],
            'team_meet_date': validated_data['team_meet_date'],
            'team_max_capacity': validated_data['team_max_capacity'],
            'team_description': validated_data['team_description'],
            'team_administrator': validated_data['team_administrator'],
            'team_resort': validated_data['team_resort']
        })
        team.save()
        return team


class ResortListSerializer(serializers.ModelSerializer):
    """Create serialized Resort objects to serve from the API. This returns the minimal detail
    expected for listing resort search results."""

    # Map field names from our db fields to the ones expected by the frontend
    name = serializers.ReadOnlyField(source='resort_name')
    latitude = serializers.ReadOnlyField(source='resort_location_latitude')
    longitude = serializers.ReadOnlyField(source='resort_location_longitude')
    websiteUrl = serializers.ReadOnlyField(source='resort_website_url')
    altitude = serializers.ReadOnlyField(source='resort_altitude')
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
        )


class ResortDetailSerializer(serializers.ModelSerializer):
    """Create serialized Resort objects to serve from the API. This returns the full data for
    a resort, including the associated Team objects. This is the view for showing detailed info on
    a selected Resort."""

    # Map field names from our db fields to the ones expected by the frontend
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
        )


class MessageSerializer(serializers.ModelSerializer):
    # TODO: build MessageSerializer class
    pass
