from rest_framework import serializers
from ..models.Post import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'content', 'post_type', 'videopath', 'createdat')