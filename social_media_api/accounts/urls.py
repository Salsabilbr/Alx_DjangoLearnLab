from django.urls import path  
from . import views  
  
urlpatterns = [  
   path('register/', views.RegisterView.as_view()),  
   path('login/', views.LoginView.as_view()),  
   path('profile/', views.ProfileView.as_view()),  
]

from django.urls import path  
from . import views  
  
urlpatterns = [  
   path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow_user'),  
   path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow_user'),  
]
