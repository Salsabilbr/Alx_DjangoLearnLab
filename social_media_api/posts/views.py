from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
   queryset = Post.objects.all()
   serializer_class = PostSerializer
   permission_classes = [IsAuthenticated]

   def perform_create(self, serializer):
      serializer.save(author=self.request.user)

   def perform_update(self, serializer):
      serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer
   permission_classes = [IsAuthenticated]

   def perform_create(self, serializer):
      serializer.save(author=self.request.user)

   def perform_update(self, serializer):
      serializer.save(author=self.request.user)

from rest_framework.pagination import PageNumberPagination  
  
class PostViewSet(viewsets.ModelViewSet):  
   ...  
   pagination_class = PageNumberPagination  
  
class CommentViewSet(viewsets.ModelViewSet):  
   ...  
   pagination_class = PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend  
  
class PostViewSet(viewsets.ModelViewSet):  
   ...  
   filter_backends = [DjangoFilterBackend]  
   filterset_fields = ['title', 'content']  
  
class CommentViewSet(viewsets.ModelViewSet):  
   ...  
   filter_backends = [DjangoFilterBackend]  
   filterset_fields = ['content']

from rest_framework.response import Response  
from rest_framework.views import APIView  
from rest_framework.permissions import IsAuthenticated  
from .models import Post, Like  
from .serializers import PostSerializer  
  
class LikePostView(APIView):  
   permission_classes = [IsAuthenticated]  
  
   def post(self, request, post_id):  
      user = request.user  
      post = Post.objects.get(id=post_id)  
      like, created = Like.objects.get_or_create(user=user, post=post)  
      if created:  
        # Generate notification  
        notification = Notification.objects.create(recipient=post.author, actor=user, verb='liked', target=post)  
      return Response({'message': 'Post liked successfully'})  
  
class UnlikePostView(APIView):  
   permission_classes = [IsAuthenticated]  
  
   def post(self, request, post_id):  
      user = request.user  
      post = Post.objects.get(id=post_id)  
      like = Like.objects.get(user=user, post=post)  
      like.delete()  
      return Response({'message': 'Post unliked successfully'})
