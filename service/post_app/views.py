from rest_framework import viewsets, generics
from rest_framework import permissions

from .serializers import PostSerializer, CommentSerializer, UserPostRelationsSerializer
from .models import Post, Comment, UserPostRelations, UserCommentRelations
from .permissions import IsOwnerOrAdmin


class PostViewSet(viewsets.ModelViewSet):
    """actions with posts"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        """checking permissions"""
        if self.request.method in permissions.SAFE_METHODS:
            permission_classes = (permissions.IsAuthenticated,)
        else:
            permission_classes = (IsOwnerOrAdmin,)
            
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
        if self.request.method in permissions.SAFE_METHODS:
            permission_classes = (permissions.IsAuthenticated,)
        else:
            permission_classes = (IsOwnerOrAdmin,)
            
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
        curr_post = Post.objects.get(pk=self.kwargs.get('post_pk'))
        user = self.request.user
        relation, _ = UserPostRelations.objects.get_or_create(user=user, post=curr_post)

        return relation    

    def perform_update(self, serializer):
        relation = self.get_object()
        curr_post = Post.objects.get(pk=self.kwargs.get('post_pk'))

        is_liked = self.kwargs.get('is_liked', None)
        in_bookmarks = self.kwargs.get('in_bookmarks', None)

        relation.is_liked = is_liked if is_liked != None else relation.is_liked
        relation.in_bookmarks = in_bookmarks if in_bookmarks != None else relation.in_bookmarks


        curr_post.likes = len(UserPostRelations.objects.filter(is_liked=True, post=curr_post))
        curr_post.save()

        serializer.save()
