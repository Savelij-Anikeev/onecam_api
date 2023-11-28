from django.urls import path

from rest_framework import routers
from .views import PostViewSet, CommentViewSet, UserPostRelationsViewSet, UserCommentRelationsViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('posts/<int:post_pk>/action/', UserPostRelationsViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 
                                                                          'put': 'update',
                                                                          'patch': 'partial_update',
                                                                          'delete': 'destroy',
                                                                        })),
    path('comments-action/<int:pk>/', UserCommentRelationsViewSet.as_view({
                                                                                                'post': 'create',
                                                                                                'get': 'retrieve',
                                                                                                'patch': 'partial_update',
                                                                                                'delete': 'destroy',
                                                                                              }))
]

