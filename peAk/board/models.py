class User(models.Model):
    """
    Holding the users for peAk website.
    """
    user_email = models.CharField(max_length=128)
    userName = models.CharField(max_length=64)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    favResort = models.CharField(max_length=128)
    dateOfBirth = models.DateField()
    groupsBelong = models.ForeignKey('Team', on_delete=models.CASCADE)
    profilePicture = models.FileField(upload_to='uploads/')
    dateJoined = models.DateField()


class Team(models.Model):
    """
    Database table for teams / groups as created by user.
    """
    name = models.CharField(max_length=128)
    meetDate = models.DateField()
    maxCapacity = models.IntegerField()
    description = models.CharField(max_length=128)
    status = models.CharField(max_length=16, default='Active')
    administrator = models.ForeignKey('User', on_delete=models.CASCADE)
    resort = models.ForeignKey('Resort', on_delete=models.CASCADE)
    users = models.ForeignKey('User', on_delete=models.CASCADE)

class Resort(models.Model):
    """
    Database table for Resort. Data pulled from API.
    """
    resort_name = models.CharField(max_length=64)
    resort_location_lat = models.IntegerField()
    resort_location_long = models.IntegerField()
    resort_address_line1 = models.CharField(max_length=64)
    resort_address_line2 = models.CharField(max_length=64)
    resort_address_city = models.CharField(max_length=64)
    resort_address_state = models.ForeignKey('State', on_delete=models.CASCADE)
    resort_address_zip_code = models.IntegerField()
    resort_website_url = models.CharField(max_length=128)
    resort_altitude = models.IntegerField()
    resort_teams = models.ForeignKey('Team', on_delete=models.CASCADE)


class State(models.Model):
    """
    Database Table for all states.
    """
    states = models.CharField(max_length=24)


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


# # class Chat(models.Model):
# #     pass
