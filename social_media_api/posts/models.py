from django.db import models

# Create your models here.
["Post(models.Model)", "Comment(models.Model)", "models.ForeignKey", "models.TextField()", "models.DateTimeField"]

# posts/models.py
from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   user = models.ForeignKey(User, on_delete=models.CASCADE)

# notifications/models.py
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
