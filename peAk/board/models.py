from django.db import models


class PeakUser(models.Model):
    """
    Holding the users for peAk website.
    """
    user_email = models.CharField(max_length=64)
    user_firstName = models.CharField(max_length=64)
    user_lastName = models.CharField(max_length=64)
    user_fav_resort = models.CharField(max_length=128, blank=True)
    user_date_of_birth = models.DateField()
    user_groups_belong = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)
    user_profile_picture = models.FileField(upload_to='uploads/', blank=True)
    user_date_joined = models.DateField()


class Team(models.Model):
    """
    Database table for teams / groups as created by user.
    """
    team_name = models.CharField(max_length=128)
    team_meet_date = models.DateField()
    team_max_capacity = models.IntegerField()
    team_description = models.CharField(max_length=128)
    team_status = models.CharField(max_length=16, default='Active')
    team_administrator = models.ForeignKey('PeakUser', on_delete=models.CASCADE)
    team_resort = models.ForeignKey('Resort', on_delete=models.CASCADE)


class Resort(models.Model):
    """
    Database table for Resort. Data pulled from API.
    """
    resort_name = models.CharField(max_length=64)
    resort_location_longitude = models.DecimalField(max_digits=30, decimal_places=15)
    resort_location_latitude = models.DecimalField(max_digits=30, decimal_places=15)
    resort_address_line1 = models.CharField(max_length=64)
    resort_address_line2 = models.CharField(max_length=64, blank=True)
    resort_address_city = models.CharField(max_length=64)
    resort_address_state = models.ForeignKey('State', on_delete=models.CASCADE)
    resort_address_zip_code = models.IntegerField()
    resort_website_url = models.CharField(max_length=128, blank=True)
    resort_altitude = models.IntegerField(blank=True)
    resort_teams = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)


class State(models.Model):
    """
    Database Table for all states.
    """
    STATES = [
        ('AK', 'AK'),
        ('AS', 'AS'),
        ('AZ', 'AZ'),
        ('CO', 'CO'),
        ('CT', 'CT'),
        ('DC', 'DC'),
        ('DE', 'DE'),
        ('FL', 'FL'),
        ('GA', 'GA'),
        ('GU', 'GU'),
        ('HI', 'HI'),
        ('IA', 'IA'),
        ('ID', 'ID'),
        ('IL', 'IL'),
        ('IN', 'IN'),
        ('KS', 'KS'),
        ('KY', 'KY'),
        ('LA', 'LA'),
        ('MA', 'MA'),
        ('MD', 'MD'),
        ('ME', 'ME'),
        ('MI', 'MI'),
        ('MN', 'MN'),
        ('MO', 'MO'),
        ('MP', 'MP'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('NA', 'NA'),
        ('NC', 'NC'),
        ('ND', 'ND'),
        ('NE', 'NE'),
        ('NH', 'NH'),
        ('NJ', 'NJ'),
        ('NM', 'NM'),
        ('NV', 'NV'),
        ('NY', 'NY'),
        ('OH', 'OH'),
        ('OK', 'OK'),
        ('OR', 'OR'),
        ('PA', 'PA'),
        ('PR', 'PR'),
        ('RI', 'RI'),
        ('SC', 'SC'),
        ('SD', 'SD'),
        ('TN', 'TN'),
        ('TX', 'TX'),
        ('UT', 'UT'),
        ('VA', 'VA'),
        ('VI', 'VI'),
        ('VT', 'VT'),
        ('WA', 'WA'),
        ('WI', 'WI'),
        ('WV', 'WV'),
        ('WY', 'WY')
    ]
    state = models.CharField(max_length=2, choices=STATES)


class MessageBoard(models.Model):
    """
    Database Table for each Team Message Board.
    """
    message_board_teams = models.ForeignKey('Team', on_delete=models.CASCADE)
    message_board_messages = models.ForeignKey('Message', on_delete=models.CASCADE)
    message_board_name = models.CharField(max_length=16)
    message_board_description = models.CharField(max_length=128)


class Message(models.Model):
    """Database Table for each Message."""
    message = models.CharField(max_length=128)
    message_date = models.DateField()
    message_user = models.ForeignKey('PeakUser', on_delete=models.CASCADE)


# # class Chat(models.Model):
# #     pass
