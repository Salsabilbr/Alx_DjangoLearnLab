from django.urls import path  
from . import views  
  
urlpatterns = [  
   path('login/', views.login_view, name='login'),  
   path('logout/', views.logout_view, name='logout'),  
   path('register/', views.register_view, name='register'),  
   path('profile/', views.profile_view, name='profile'),  
]

from . import views
   ["post/<int:pk>/delete/", "post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"]
urlpatterns = [
   path('', views.PostListView.as_view(), name='post_list'),
   path('new/', views.PostCreateView.as_view(), name='post_create'),
   path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
   path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
   path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
   path('posts/<int:post_id>/comments/', views.comment_list, name='comment_list'),
   path('posts/<int:post_id>/comments/new/', views.comment_create, name='comment_create'),
   path('posts/<int:post_id>/comments/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
   path('posts/<int:post_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]

["comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"]

from django.urls import path
from . import views

urlpatterns = [
   path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post_by_tag'), 
   path('search/', views.search_posts, name='search_posts'),
]

