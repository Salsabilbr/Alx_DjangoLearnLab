from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
  
class RegistrationForm(UserCreationForm):  
   email = forms.EmailField(max_length=200)  
  
   class Meta:  
      model = User  
      fields = ('username', 'email', 'password1', 'password2')

from django import forms  
from django.contrib.auth.models import User  
  
class ProfileForm(forms.ModelForm):  
   email = forms.EmailField(max_length=200)  
  
   class Meta:  
      model = User  
      fields = ('email',)

from django import forms  
from .models import Post

class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('title', 'content')

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ('content',)

from django import forms  
from taggit.forms import TagWidget  
  
class PostForm(forms.ModelForm):  
   tags = forms.CharField(widget=TagWidget)  
  
   class Meta:  
      model = Post  
      fields = ('title', 'content', 'tags')

from django import forms  
from taggit.forms import TagWidget  
  
from django import forms
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
   tags = forms.CharField(widget=TagWidget())

   class Meta:
      model = Post
      fields = ('title', 'content', 'tags')
      widgets = {
        'tags': TagWidget(),
      }
