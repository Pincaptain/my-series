from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import datetime


class ProfileModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    image_path = models.CharField(max_length=255)
    date_registered = models.DateTimeField(default=datetime.datetime.now())


# noinspection PyUnusedLocal
def create_profile(sender, **kwargs):
    if kwargs['created']:
        ProfileModel.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)