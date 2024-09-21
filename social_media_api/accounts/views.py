from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response  
from rest_framework.views import APIView  
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.models import Token  
from .serializers import UserSerializer  
  
class RegisterView(APIView):  
   def post(self, request):  
      serializer = UserSerializer(data=request.data)  
      if serializer.is_valid():  
        user = serializer.save()  
        token, created = Token.objects.get_or_create(user=user)  
        return Response({'token': token.key})  
      return Response(serializer.errors, status=400)  
  
class LoginView(ObtainAuthToken):  
   def post(self, request, *args, **kwargs): 
serializer = self.serializer_class(data=request.data, context={'request': request})  
      serializer.is_valid(raise_exception=True)  
      user = serializer.validated_data['user']  
      token, created = Token.objects.get_or_create(user=user)  
      return Response({'token': token.key})  
  
# accounts/serializers.py  
from rest_framework import serializers  
from .models import User  
  
class UserSerializer(serializers.ModelSerializer):  
   class Meta:  
      model = User  
      fields = ['username', 'email', 'password', 'bio', 'profile_picture']  
      extra_kwargs = {'password': {'write_only': True}}  
  
   def create(self, validated_data):  
      user = User.objects.create_user(**validated_data)  
      return user

class RegisterView(APIView):
   def post(self, request):
      ...
      return Response({'token': token.key})

class LoginView(ObtainAuthToken):
   def post(self, request, *args, **kwargs):
      ...
      return Response({'token': token.key})

from rest_framework.response import Response  
from rest_framework.views import APIView  
from .models import User  
  
class FollowUserView(APIView):  
   def post(self, request, user_id):  
      user = request.user  
      followee = User.objects.get(id=user_id)  
      user.following.add(followee)  
      return Response({'message': 'User followed successfully'})  
  
class UnfollowUserView(APIView):  
   def post(self, request, user_id):  
      user = request.user  
      followee = User.objects.get(id=user_id)  
      user.following.remove(followee)  
      return Response({'message': 'User unfollowed successfully'})

["generics.GenericAPIView", "permissions.IsAuthenticated", "CustomUser.objects.all()"]
