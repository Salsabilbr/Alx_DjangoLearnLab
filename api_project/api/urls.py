from django.urls import path  
from . import views  
  
urlpatterns = [  
   path('books/', views.BookList.as_view()),  
]

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
