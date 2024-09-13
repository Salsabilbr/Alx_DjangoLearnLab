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

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostCreateView(LoginRequiredMixin, CreateView):
   # ...

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   # ...

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  
   # ...  
  
   def test_func(self):  
      post = self.get_object()  
      return self.request.user == post.author

from django.shortcuts import render, redirect  
from django.contrib.auth.decorators import login_required  
from .models import Comment  
from .forms import CommentForm  
  
def comment_list(request, post_id):  
   post = Post.objects.get(id=post_id)  
   comments = post.comment_set.all()  
   return render(request, 'comment_list.html', {'comments': comments})  
  
@login_required  
def comment_create(request, post_id):  
   post = Post.objects.get(id=post_id)  
   if request.method == 'POST':  
      form = CommentForm(request.POST)  
      if form.is_valid():  
        comment = form.save(commit=False)  
        comment.post = post  
        comment.author = request.user  
        comment.save()  
        return redirect('comment_list', post_id=post_id)  
   else:  
      form = CommentForm()  
   return render(request, 'comment_form.html', {'form': form})  
  
@login_required  
def comment_edit(request, post_id, comment_id):  
   post = Post.objects.get(id=post_id)  
   comment = Comment.objects.get(id=comment_id)  
   if request.method == 'POST':  
      form = CommentForm(request.POST, instance=comment)  
      if form.is_valid():  
        form.save()  
        return redirect('comment_list', post_id=post_id)  
   else:  
      form = CommentForm(instance=comment)  
   return render(request, 'comment_form.html', {'form': form})  
  
@login_required  
def comment_delete(request, post_id, comment_id):  
   post = Post.objects.get(id=post_id)  
   comment = Comment.objects.get(id=comment_id)  
   comment.delete()  
   return redirect('comment_list', post_id=post_id)

["CommentCreateView", "CommentUpdateView", "CommentDeleteView"]
