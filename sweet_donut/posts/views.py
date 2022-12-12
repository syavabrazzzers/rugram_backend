import os

import drf_yasg.openapi
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from . import serializers
from .serializers import PostSerializer, UserSerializer, PostUpdateSerializer, UploadSerializer, ImagesSerializer
from .models import Post, Image
from django.contrib.auth import get_user_model
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, swagger_settings

# Create your views here.


class PostView(APIView):

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="VLADICK PIDOR HUI SOSI",
        request_body=PostUpdateSerializer)
    def put(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostUpdateSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        if request.user.is_authenticated:
            post.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="VLADICK PIDOR HUI SOSI",
        request_body=UploadSerializer)
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Post not found"})
        if post.author.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        Image.objects.create(image=request.data['file'], post=post)
        return Response(status=status.HTTP_201_CREATED)



class FileDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk=None):
        file = Image.objects.get(id=pk)
        if file.post.author.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        os.remove(str(file))
        file.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class PostsView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        donuts = Post.objects.all()
        serializer = PostSerializer(donuts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="VLADICK PIDOR HUI SOSI",
        request_body=serializers.PostCreateSerializer)
    def post(self, request):
        file = request.data.get('file')
        print(file)
        serializer = serializers.PostCreateSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
        # if not file:
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'File required'})
            post = Post.objects.create(author=request.user, description=request.data['description'])
            Image.objects.create(image=request.data['file'], post=post)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)