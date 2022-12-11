from abc import ABC

from rest_framework.serializers import Serializer, ModelSerializer, ListSerializer, FileField, ListField, IntegerField
from .models import Post, Image
from django.contrib.auth import get_user_model


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')

class PostSerializer(ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'author', 'images')


class UploadSerializer(Serializer):
    file = FileField(max_length=None, allow_empty_file=False, allow_null=False, required=True, read_only=False)
    class Meta:
        fields = ['file']


class DropFileSerializer(Serializer):
    id = IntegerField()
    class Meta():
        fields = ['id']


class PostUpdateSerializer(ModelSerializer):
    images = ListField(child=FileField(max_length=None, allow_empty_file=False, allow_null=False, required=True))
    class Meta:
        model = Post
        fields = ('images',)

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'bio', 'site')
