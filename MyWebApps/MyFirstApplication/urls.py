from django.urls import path, include, re_path
from rest_framework import routers
from .views.User_view import UserView
from .views import login_view

router = routers.DefaultRouter()
router.register(r'users', UserView)


urlpatterns = [
    ## Usuarios ----------------------------------------------------
    re_path('signup', login_view.signup),
    re_path('login', login_view.login),
    re_path('test_token', login_view.test_token),
    path("users/", include(router.urls)),
    
]
