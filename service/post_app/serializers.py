from rest_framework import serializers

from .models import Post, Comment, UserPostRelations, UserCommentRelations


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'likes', 'views', 'published', 'updated', 'owner')
        read_only_fields = ('id', 'likes', 'views', 'published', 'updated', 'owner') 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'owner', 'text', 'published', 'updated', 'likes')
        read_only_fields = ('id', 'likes', 'published', 'updated', 'owner') 

