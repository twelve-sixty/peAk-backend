from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ResortSerializer, UserSerializer, TeamSerializer, MessageSerializer


class ResortListApiView(generics.ListAPIView):
    pass


class ResortDetailApiView(generics.RetrieveAPIView):
    pass


class UserDetailApiView(generics.RetrieveAPIView):
    pass


class TeamListView(generics.ListCreateAPIView):
    pass


class TeamDetailView(generics.RetrieveAPIView):
    pass


class MessageListView(generics.ListAPIView):
    pass


class MessageDetailView(generics.RetrieveAPIView):
    pass
