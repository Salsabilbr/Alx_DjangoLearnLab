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
