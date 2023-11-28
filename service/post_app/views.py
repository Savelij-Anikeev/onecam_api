from rest_framework import viewsets, generics
from rest_framework import permissions

from .serializers import PostSerializer
from .models import Post, UserPostRelations
from .permissions import IsOwnerOrAdmin



class PostViewSet(viewsets.ModelViewSet):
    """actions with post"""
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
    
