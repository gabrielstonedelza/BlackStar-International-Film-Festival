from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image

DeUser = settings.AUTH_USER_MODEL


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    full_name = models.CharField(max_length=150, unique=True)

    REQUIRED_FIELDS = ['username', 'full_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="profile_user")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)