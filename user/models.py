from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    image_path = models.CharField(max_length=255)
    date_registered = models.DateTimeField(auto_now_add=True)
