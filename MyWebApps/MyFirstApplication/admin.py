from django.contrib import admin

# Register your models here.

from .models.Post import Post
from .models.User import User
admin.site.register(Post)
admin.site.register(User)