from django.urls import path, include, re_path
from rest_framework import routers
from .views.User_view import UserView
from .views import login_view, post_view

router = routers.DefaultRouter()
router.register(r'users', UserView)


urlpatterns = [
    ## Usuarios ----------------------------------------------------
    re_path('signup', login_view.signup),
    re_path('login', login_view.login),
    re_path('test_token', login_view.test_token),
    re_path('post', post_view.create_post),
    re_path('all', post_view.get_all_posts),
    re_path('ban', login_view.ban),
    path("users/", include(router.urls)),
    
]
