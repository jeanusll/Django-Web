from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid
from .User import User

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(null=True, blank=True, max_length=700)
    post_type = models.CharField(null=False, max_length=15)
    videopath = models.CharField(null=False, max_length=700)
    createdat = models.DateTimeField(auto_now=True, auto_now_add=False)

class Meta:
    ordering = ['id', 'user_id', 'content', 'post_type', 'videopath']

def __str__(self):
    return " %d %d %s" % (self.id, self.user_id, self.post_type)