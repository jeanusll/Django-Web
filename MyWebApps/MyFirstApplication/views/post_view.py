from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from ..models import User, Post
from ..serializers import PostSerializer
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from ..decorators import token_required


@api_view(['POST'])
@token_required
def create_post(request):
    token = request.COOKIES.get('token')

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('user_id')

        user = User.objects.get(pk=user_id)

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@token_required
def get_all_posts(request):
    paginator = PageNumberPagination()
    paginator.page_size = 50

    posts = Post.objects.all()
    paginated_posts = paginator.paginate_queryset(posts, request)
    
    serializer = PostSerializer(paginated_posts, many=True)
    return paginator.get_paginated_response(serializer.data)