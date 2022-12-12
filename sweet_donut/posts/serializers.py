from abc import ABC

from rest_framework.serializers import Serializer, ModelSerializer, ListSerializer, FileField, ListField, IntegerField, CharField
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
        fields = ('id', 'author', 'images', 'description', 'created_at', 'updated_at')


class PostCreateSerializer(ModelSerializer):
    file = FileField(max_length=None, allow_empty_file=False, allow_null=False, required=True)
    # description = CharField(max_length=500)
    class Meta:
        model = Post
        fields = ['file', 'description']


class UploadSerializer(Serializer):
    file = FileField(max_length=None, allow_empty_file=False, allow_null=False, required=True, read_only=False)
    class Meta:
        fields = ['file']


class DropFileSerializer(Serializer):
    id = IntegerField()
    class Meta():
        fields = ['id']


class PostUpdateSerializer(ModelSerializer):
    # images = ListField(child=FileField(max_length=None, allow_empty_file=False, allow_null=False, required=True))
    class Meta:
        model = Post
        fields = ['description']

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'bio', 'site')
