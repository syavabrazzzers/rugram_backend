from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# from sweetusers.models import MyUser
# from django.contrib.auth.models import User

# Create your models here.


from django.conf import settings
# class Post(models.Model):
#     id = models.AutoField(primary_key=True)
#     donut_to = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='foreign_donut_to')
#     donut_from = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='foreign_donut_from')
#     message = models.TextField(max_length=255)
#     amount = models.DecimalField(max_digits=7, decimal_places=2)
#     created_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'ID: {self.id}'

# class ImageAlbum(models.Model):
#     def default(self):
#         return self.images.filter(default=True).first()
#     def thumbnails(self):
#         return self.images.filter(width__lt=100, length_lt=100)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=500, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.username} ({self.id})'


class Image(models.Model):
    image = models.FileField(upload_to='templates/images/')
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name

