from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group

from django.shortcuts import get_object_or_404
from ..models import User 
from ..serializers.User_serializer import UserSerializer
from rest_framework.authtoken.models import Token
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.authtoken.models import Token
from ..decorators import token_required
from django.http import JsonResponse


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()

        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1),  
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        # Guardar el token en los cookies del Response
        response = JsonResponse({'token': token, 'user': serializer.data})
        response.set_cookie('token', token, httponly=True)  # Almacena el token en una cookie HTTPOnly

        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("Invalid credentials", status=status.HTTP_404_NOT_FOUND)

    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=1),  
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    serializer = UserSerializer(user)

    response = JsonResponse({'token': token, 'user': serializer.data})
    response.set_cookie('token', token, httponly=True, samesite='None')  

    return response


@api_view(['POST'])
def ban(request):
    user_id = request.data['user_id_staff']
    user = User.objects.filter(id=user_id).first()

    if user and user.is_active:
        user_id2 = request.data['user_id_banned']
        user2 = User.objects.filter(id=user_id2).first()

        if user2:
            try:
                group = Group.objects.get(name='default')
                group.user_set.remove(user2)
                return Response("User removed from the group successfully")
            except Group.DoesNotExist:
                return Response("Group 'default' does not exist")
            except Exception as e:
                return Response(f"An error occurred: {str(e)}")
        
        return Response("User to be removed not found")

    return Response("User is not active or not authorized")

@api_view(['GET'])
@token_required
def test_token(request):
    return Response("passed!")