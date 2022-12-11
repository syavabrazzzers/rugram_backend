from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from datetime import datetime

# Create your models here.


class User(AbstractUser):
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
        default=f'User{round(datetime.now().timestamp())}'
    )

    def __str__(self):
        return f'ID: {self.id}  ({self.username})'


class Profile(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(storage="templates/avatars/", null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)

    # donation_link = models.CharField(max_length=255, null=True, blank=True)
    # widget_token = models.CharField(max_length=255, null=True, blank=True)
    # donutions_count = models.IntegerField(default=0)
    # donutions_total = models.DecimalField(max_digits=20, decimal_places=3, default=0)

    def __str__(self):
        return f'ID: {self.user.id}  ({self.user.username})'


class Subscriptions(models.Model):
    subject = models.ForeignKey(User, related_name='author_subscription', on_delete=models.CASCADE, null=True)
    object = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE, null=True)
    subscribe_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ---> {self.object}"
