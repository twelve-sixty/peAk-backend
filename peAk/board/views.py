from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ResortSerializer, UserSerializer, TeamOverviewSerializer, MessageSerializer, TeamDetailSerializer
from .models import Resort, PeakUser, Team

#TODO: Uncomment auth lines when app auth is working

class ResortListApiView(generics.ListCreateAPIView):
    """List or create Resort objects in API."""
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )
    serializer_class = ResortSerializer
    #https://stackoverflow.com/questions/3711349/django-and-query-string-parameters

    def get_queryset(self):
        lat = self.request.GET.get('latitude')
        long = self.request.GET.get('longitude')
        radius = self.request.GET.get('radius')
        if lat and long:
            if radius:
                # TODO: Figure out how to filter Resort objects by distance from phone
                pass

        #TODO: Change .all() to .filter when the filter is figured out
        return Resort.objects.all()


class ResortDetailApiView(generics.RetrieveAPIView):
    serializer_class = ResortSerializer

    def get_queryset(self):
        return Resort.objects.filter(id=self.kwargs['pk'])

#TODO: Build out view

class UserDetailApiView(generics.RetrieveAPIView):

    # password = serializers.CharField(write_only=True)
    serializer_class = UserSerializer


    def get_queryset(self):
        return PeakUser.objects.filter(id=self.kwargs['pk'])

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email']
        })
        user.set_password(validated_data['password'])
        user.save()
        return user


#TODO: Build out view

class TeamListView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Team.objects.filter(team_resort=self.kwargs['pk'])


class TeamDetailView(generics.RetrieveAPIView):
    #TODO: add isAdministrator property to JSON response if requester owns the Team
    serializer_class = TeamDetailSerializer
    def get_queryset(self):
        return Team.objects.filter(id=self.kwargs['pk'])

#TODO: Build out view
class MessageListView(generics.ListAPIView):
    pass

#TODO: Build out view
class MessageDetailView(generics.RetrieveAPIView):
    pass

class UserApiView(generics.RetrieveAPIView):
    """CBV to handle requests for users on REST API.

    """
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return PeakUser.objects.filter(id=self.kwargs['pk'])


class RegisterApiView(generics.CreateAPIView):
    """CBV to handle registration requests on REST API.

    """
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class ResortTeamListApiView(generics.ListAPIView):
    """CBV to list Teams associated with a resort."""
    serializer_class = TeamOverviewSerializer
    def get_queryset(self):
        return Team.objects.filter(team_resort__id=self.kwargs['resort_id'])
