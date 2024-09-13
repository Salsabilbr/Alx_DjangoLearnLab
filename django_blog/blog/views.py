from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

def login_view(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
   return render(request, 'login.html')

def logout_view(request):
   logout(request)
   return redirect('home')

def register_view(request):
   if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('login')
   else:
      form = RegistrationForm()
   return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def profile_view(request):
   if request.method == 'POST':
      form = ProfileForm(request.POST, instance=request.user)
      if form.is_valid():
        form.save()
        return redirect('profile')
   else:
      form = ProfileForm(instance=request.user)
   return render(request, 'profile.html', {'form': form})

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostListView(ListView):
   model = Post
   template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
   model = Post
   template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
   model = Post
   fields = ('title', 'content')
   template_name = 'blog/post_form.html'

class PostUpdateView(UpdateView):
   model = Post
   fields = ('title', 'content')
   template_name = 'blog/post_form.html'

class PostDeleteView(DeleteView):
   model = Post
   template_name = 'blog/post_delete.html'

 # Create your views here.
