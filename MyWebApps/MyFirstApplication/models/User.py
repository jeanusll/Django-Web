from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    points = models.IntegerField(null=False, default=0)
    bio = models.CharField(null=True, blank=True, max_length=400)
    avatar = models.CharField(null=True, blank=True, max_length=700)
    dateofbirth = models.DateField(auto_now=False, auto_now_add=False, null=False)
    is_superuser = models.BooleanField(null=False, default=False)
    money = models.DecimalField(max_digits=5, decimal_places=2, default = 0.0)
    is_active = models.BooleanField(null=False, default=True)

    REQUIRED_FIELDS = ['points', 'email', 'dateofbirth', 'avatar', 'bio']

    class Meta:
        ordering = ['id', 'username', 'date_joined']

    def __str__(self):
        return f"{self.username} {self.points} {self.email} {self.is_active}"