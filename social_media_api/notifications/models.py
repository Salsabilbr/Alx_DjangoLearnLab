from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Notification(models.Model):
   recipient = models.ForeignKey(User, on_delete=models.CASCADE)
   actor = models.ForeignKey(User, on_delete=models.CASCADE)
   verb = models.CharField(max_length=255)
   target = GenericForeignKey('content_type', 'object_id')
   content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
   object_id = models.PositiveIntegerField()
   timestamp = models.DateTimeField(auto_now_add=True)

