from rest_framework.authtoken.models import Token 

class CommentSerializer(serializers.serializer):
    ["serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"]
from rest_framework import serializers  
from .models import Post, Comment  
  
class PostSerializer(serializers.ModelSerializer):  
   author = serializers.StringRelatedField(read_only=True)  
  
   class Meta:  
      model = Post  
      fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']  
  
class CommentSerializer(serializers.ModelSerializer):  
   author = serializers.StringRelatedField(read_only=True)  
   post = serializers.PrimaryKeyRelatedField(read_only=True)  
  
   class Meta:  
      model = Comment  
      fields = ['id', 'content', 'author', 'post', 'created_at', 'updated_at']
