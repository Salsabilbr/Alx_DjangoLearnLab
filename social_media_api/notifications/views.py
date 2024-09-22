from django.shortcuts import render
# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Notification

def get_notifications(request):
   user = request.user
   notifications = Notification.objects.filter(recipient=user).order_by('-timestamp')
   return HttpResponse(notifications)

