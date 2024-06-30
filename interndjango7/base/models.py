from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to="profile_pictures/")
    address = models.TextField()
    doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
