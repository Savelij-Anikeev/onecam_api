from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework import permissions

from .serializers import PostSerializer, CommentSerializer, UserPostRelationsSerializer, UserCommentRelationsSerializer
from .models import Post, Comment, UserPostRelations, UserCommentRelations
from .permissions import IsOwnerOrAdmin


class PostViewSet(viewsets.ModelViewSet):
    """actions with posts"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        """checking permissions"""
        if self.request.method not in permissions.SAFE_METHODS:
            permission_classes = (IsOwnerOrAdmin)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """automatically adding user while creating"""
        serializer.validated_data['owner'] = self.request.user
        serializer.save()
    

class CommentViewSet(viewsets.ModelViewSet):
    """actions with comments"""  
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer

    def get_permissions(self):
        """checking permissions"""
        if self.request.method not in permissions.SAFE_METHODS:
            permission_classes = (IsOwnerOrAdmin)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """automatically adding user while creating"""
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserPostRelationsViewSet(viewsets.ModelViewSet):
    """view that manages to add user/post relations"""
    queryset = UserPostRelations.objects.all()
    serializer_class = UserPostRelationsSerializer
    http_method_names = ['post', 'get', 'patch']

    def get_object(self):
        curr_post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        user = self.request.user
        obj, _ = UserPostRelations.objects.get_or_create(user=user, post=curr_post)

        return obj    

    def perform_update(self, serializer):
        relation = self.get_object()
        user = self.request.user
        curr_post = Post.objects.get(pk=self.kwargs.get('post_pk'))

        is_liked = self.kwargs.get('is_liked', None)
        in_bookmarks = self.kwargs.get('in_bookmarks', None)

        relation.is_liked = is_liked if is_liked != None else relation.is_liked
        relation.in_bookmarks = in_bookmarks if in_bookmarks != None else relation.in_bookmarks
        print(f'\n\n\n\n{curr_post} aaa\n\n\n\n\n')

        curr_post.likes = len(UserPostRelations.objects.filter(post=curr_post, is_liked=True))
        curr_post.save()

        serializer.save()


class UserCommentRelationsViewSet(viewsets.ModelViewSet):
    queryset = UserCommentRelations.objects.all()
    serializer_class = UserCommentRelationsSerializer

    def get_object(self):
        comment_instance = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        obj, _ = UserCommentRelations.objects.get_or_create(user=self.request.user, comment=comment_instance)

        return obj

    def perform_update(self, serializer):
        relation_instance = self.get_object()

        is_liked = self.kwargs.get('is_liked', None)
        relation_instance.is_liked = is_liked if is_liked != None else relation_instance.is_liked
        relation_instance.save()

        serializer.save()