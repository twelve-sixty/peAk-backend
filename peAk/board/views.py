from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ResortSerializer, UserSerializer, TeamSerializer, MessageSerializer
from .models import Resort

#TODO: Uncomment auth lines when app auth is working

class ResortListApiView(generics.ListAPIView):
    """List or create Budget objects in API."""
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
    pass

#TODO: Build out view

class TeamListView(generics.ListCreateAPIView):
    pass

#TODO: Build out view
class TeamDetailView(generics.RetrieveAPIView):
    pass

#TODO: Build out view
class MessageListView(generics.ListAPIView):
    pass

#TODO: Build out view
class MessageDetailView(generics.RetrieveAPIView):
    pass
