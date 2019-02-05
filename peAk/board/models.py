# from django.db import models
# # import datetime


# class Users(models.Model):
#     """
#     Holding the users for peAk website.
#     """
#     user_email = models.CharField(max_length=128)
#     user_name_first = models.CharField(max_length=64)
#     user_name_last = models.CharField(max_length=64)
#     user_fav_resort = models.CharField(max_length=128)
#     user_date_of_birth = models.DateField()
#     user_groups_belong = models.ForeignKey('Group')
#     user_profile_picture = models.FileField(upload_to='uploads/')
#     user_date_joined = models.DateField()


# class Teams(models.Model):
#     """
#     Database table for teams / groups as created by user.
#     """
#     team_name = models.CharField(max_length=128)
#     team_meet_date = models.DateField()
#     team_max_capacity = models.IntegerField(max_length=10)
#     team_description = models.CharField(max_length=128)
#     team_status = models.CharField(max_length=16, default='Active')
#     team_administrator = models.ForeignKey(Users)
#     team_resort = models.ForeignKey('Resorts')


# class Resorts(models.Model):
#     """
#     Database table for Resorts. Data pulled from API.
#     """
#     resort_name = models.CharField(max_length=64)
#     resort_location_lat = models.IntegerField(max_length=16)
#     resort_location_long = models.IntegerField(max_length=16)
#     resort_address_line1 = models.CharField(max_length=64)
#     resort_address_line2 = models.CharField(max_length=64)
#     resort_address_city = models.CharField(max_length=64)
#     resort_address_state = models.ForeignKey('States')
#     resort_address_zip_code = models.IntegerField(max_length=10)
#     resort_website_url = models.CharField(max_length=128)
#     resort_altitude = models.IntegerField(max_length=20)
#     resort_teams = models.ForeignKey('Teams')


# class States(models.Model):
#     """
#     Database Table for all states.
#     """
#     states = models.CharField(max_length=24)


# class MessageBoard(models.Model):
#     """
#     Database Table for each Team Message Board.
#     """
#     message_board_teams = models.ForeignKey('Teams')
#     message_board_messages = models.ForeignKey('Messages')
#     message_board_name = models.CharField(max_length=16)
#     message_board_description = models.CharField(max_length=128)


# class Messages(models.Model):
#     """Database Table for each Message."""
#     message = models.CharField(max_length=128)
#     message_date = models.DateField()


# # class Chat(models.Model):
# #     pass
