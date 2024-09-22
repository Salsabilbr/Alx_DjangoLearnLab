from django.urls import path  
from . import views  
  
urlpatterns = [  
   path('notifications/', views.get_notifications, name='get_notifications'),  
]

