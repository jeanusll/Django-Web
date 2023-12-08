from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
from ..models import User 
from ..serializers.User_serializer import UserSerializer
from rest_framework.authtoken.models import Token
import jwt
from datetime import datetime, timedelta
from django.conf import settings
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

        response = JsonResponse({'token': token, 'user': serializer.data})
        response.set_cookie('token', token, httponly=True)
        
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

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    serializer = UserSerializer(user)
    
    response = JsonResponse(serializer.data)
    response.set_cookie('token', token, httponly=True)  
    
    return response

@api_view(['GET'])
@token_required
def test_token(request):
    return Response("passed!")
