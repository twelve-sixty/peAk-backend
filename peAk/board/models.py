from django.db import models


class Resort(models.Model):
    name = models.CharField(max_length=128, default='resort_name')
    url = models.CharField(max_length=128, default='group_url')
    pass


class Group(models.Model):
    name = models.CharField(max_length=128, default='group_name')
    url = models.CharField(max_length=128, default='group_url')
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)


class User(models.Model):
    """
    Holding the users for peAk website.
    """
    email = models.CharField(max_length=128, default='user_email')
    username = models.CharField(max_length=128, default='user_name')
    fav_resort = models.CharField(max_length=128, default='fav_resort')
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


# class Chat(models.Model):
#     pass
