from django.urls import include, path
from .views import ResortListApiView, ResortDetailApiView, UserDetailApiView, TeamListView, TeamDetailView, MessageListView, MessageDetailView, ResortTeamListApiView, TeamCreateView, RegisterUserApiView
from rest_framework.authtoken import views

urlpatterns = [
    path(
        'resort/',
        ResortListApiView.as_view(),
        name='resort_list'),
    path(
        'resort/<int:pk>',
        ResortDetailApiView.as_view(),
        name='resort_detail'),
    path('resort/<int:resort_id>/team/', ResortTeamListApiView.as_view(), name='resort_team_list'),
    path(
        'user/<int:pk>',
        UserDetailApiView().as_view(),
        name='user_detail'),
    path(
        'team/',
        TeamCreateView().as_view(),
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
        name='message_detail'),
    path(
        'register/', RegisterUserApiView().as_view(), name='register'
    ),
    path('login/', views.obtain_auth_token)
]
