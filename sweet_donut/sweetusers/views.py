from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserRegisterSerializer, UserSerializer, UserProfileSerializer
from .models import Profile, Subscription
from django.contrib.auth import password_validation
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from djoser import views
# Create your views here.
User = get_user_model()


class UserView(APIView):
    username_parameter = openapi.Parameter('username', openapi.IN_QUERY, description="username", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[username_parameter])
    def get(self, request):
        username = dict(request.query_params)['username'][0]
        try:
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                return Response({'error': {'code': 404, 'message': 'User doesn`t exist'}}, status=status.HTTP_404_NOT_FOUND)
            print(type(user.id))
            profile = Profile.objects.get(user=user)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            profile = Profile(user=user)
            profile.save()
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)


class SubscribeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        object = User.objects.get(id=pk)
        try_subs = Subscription.objects.filter(object=object)
        if try_subs:
            return Response(status=status.HTTP_200_OK, data={'message': 'subscribed'})
        return Response(status=status.HTTP_200_OK, data={'message': 'not subscribed'})
    def post(self, request, pk):
        object = User.objects.get(id=pk)
        print(object)
        try_subs = Subscription.objects.filter(object=object)
        print(try_subs)
        if try_subs:
            return Response(status=status.HTTP_208_ALREADY_REPORTED, data={'error': 'Subscription already exists'})
        Subscription.objects.create(subject=request.user, object=object)
        return Response(status=status.HTTP_201_CREATED)

    # @swagger_auto_schema(
    #     operation_description="VLADICK PIDOR HUI SOSI",
    #     request_body=UserRegisterSerializer)
    # def post(self, request):
    #     data = request.data
    #     serializer = UserSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         user = User.objects.get(username=serializer.data['username'])
    #         user.set_password(make_password(data['password']))
    #         user.save()
    #         profile = Profile(user=user)
    #         profile.save()
    #         print('USER CREATED')
    #         return Response(serializer.data)


#
#     @swagger_auto_schema(
#         operation_description="VLADICK PIDOR HUI SOSI",
#         request_body=UserRegisterSerializer)
#     def post(self, request):
#         try:
#             User.objects.get(username=request.data['username'])
#             return Response({'message': 'User already exists'})
#         except ObjectDoesNotExist:
#             serializer = UserRegisterSerializer(data=request.data)
#             if serializer.is_valid():
#                 user = serializer.save()
#                 user.set_password(make_password(serializer.data['password']))
#                 new_user = User.objects.get(username=request.data['username'])
#                 new_user_serializer = UserSerializer(data=new_user)
#                 # print(new_user_serializer.data)
#                 if new_user_serializer.is_valid():
#                     return Response(new_user_serializer.data)
#         return Response({'error': 'suka blyat'})
#         # new_user.set_password(request.data['password'])



