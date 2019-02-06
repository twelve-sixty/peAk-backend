from django.urls import include, path
from .views import ResortListApiView, ResortDetailApiView, UserDetailApiView, TeamListView, TeamDetailView, MessageListView, MessageDetailView


urlpatterns = [
    path(
        'resort/',
        ResortListApiView.as_view(),
        name='resort_list'),
    path(
        'resort/<int:pk>',
        ResortDetailApiView.as_view(),
        name='resort_detail'),
    path(
        'user/<int:pk>',
        UserDetailApiView().as_view(),
        name='user_detail'),
    path(
        'team/',
        TeamListView().as_view(),
        name='team_add'),
    path(
        'team/<int:pk>',
        TeamDetailView().as_view(),
        name='team_detail'),
    path(
        'message/',
        MessageListView().as_view(),
        name='message_list'),
    path(
        'message/<int:pk>',
        MessageDetailView().as_view(),
        name='message_detail')]
