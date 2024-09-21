from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from . import views  
  
router = DefaultRouter()  
router.register(r'posts', views.PostViewSet)  
router.register(r'comments', views.CommentViewSet)  
  
urlpatterns = [  
   path('', include(router.urls)),  
]

from django.urls import path
from . import views

urlpatterns = [
   path('feed/', views.FeedView.as_view(), name='feed'),
]
