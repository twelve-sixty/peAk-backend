from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

TAGS = [
    ('2BD', '2 black diamond'),
    ('1BD', '1 black diamond'),
    ('BS', 'blue square'),
    ('GS', 'green circle'),
    ('OP', 'off piste'),
    ('PH', 'party hardy'),
    ('FF', 'family friendly'),
    ('TP', 'terrain park')
]


class Resort(models.Model):
    """
    Database table for Resort. Data pulled from API.
    """
    resort_name = models.CharField(max_length=64)
    resort_location_latitude = models.CharField(max_length=64)
    resort_location_longitude = models.CharField(max_length=64)
    resort_address_line1 = models.CharField(max_length=64)
    resort_address_line2 = models.CharField(max_length=64, blank=True, null=True, default='')
    resort_address_city = models.CharField(max_length=64)
    resort_address_state = models.CharField(max_length=2, choices=STATES)
    resort_address_zip_code = models.IntegerField()
    resort_website_url = models.CharField(max_length=128, blank=True)
    resort_altitude = models.IntegerField(blank=True)
    resort_team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)


class Team(models.Model):
    """
    Database table for teams / groups as created by user.
    """
    team_name = models.CharField(max_length=128)
    team_meet_date = models.DateField()
    team_max_capacity = models.IntegerField()
    team_description = models.CharField(max_length=128)
    team_status = models.CharField(max_length=16, default='Active')
    team_tags = MultiSelectField(choices=TAGS, blank=True, null=True)
    team_resort = models.ForeignKey('Resort', on_delete=models.CASCADE, related_name='teams')
    team_administrator = models.ForeignKey('PeakUser', on_delete=models.CASCADE)
    # team_users = models.ForeignKey('PeakUser', on_delete=models.CASCADE)


class MessageBoard(models.Model):
    """
    Database Table for each Team Message Board.
    """
    message_board_name = models.CharField(max_length=16)
    message_board_description = models.CharField(max_length=128)
    message_board_teams = models.ForeignKey('Team', on_delete=models.CASCADE)


class Message(models.Model):
    """Database Table for each Message."""
    message = models.CharField(max_length=128)
    message_date = models.DateField()
    message_board = models.ForeignKey('MessageBoard', on_delete=models.CASCADE, blank=True, null=True)
    message_user = models.ForeignKey('PeakUser', on_delete=models.CASCADE)


class PeakUser(models.Model):
    """
    Holding the users for peAk website.
    """
    # user_email = models.CharFielld(max_length=64)
    user_firstName = models.CharField(max_length=64, blank=True, null=True)
    user_lastName = models.CharField(max_length=64, blank=True, null=True)
    # user_userName = models.CharField(max_length=64)
    user_fav_resort = models.CharField(max_length=128, blank=True, null=True)
    user_date_of_birth = models.DateField(blank=True, null=True)
    # user_profile_picture = models.FileField(upload_to='uploads/', blank=True)
    # user_date_joined = models.DateField(blank=True, null=True)
    user_team_belong = models.TextField('Team', blank=True, null=True, default='[]')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PeakUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.peakuser.save()
