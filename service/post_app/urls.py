from django.urls import path

from rest_framework import routers
from .views import PostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 
                                                                          'put': 'update',
                                                                          'patch': 'partial_update',
                                                                          'delete': 'destroy',
                                                                        })),
]

urlpatterns += router.urls
