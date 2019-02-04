from django.db import models


class User(models.Model):
    """
    Holding the users for peAk website.
    """
    email = models.CharField(max_length=128, default='user_email')
    username = models.CharField(max_length=128, default='user_name')
    fav_resort = models.CharField(max_length=128, default='fav_resort')
    age = models.IntegerField(max_length=20, default='user_age')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length='128', default='group_name')
    url = models.CharField(max_length='128', default='group_url')
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)


class Resort(models.Model):
    pass


# class Chat(models.Model):
#     pass