from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),

    # djoser authentication
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # post_app urls
    path('api/v1/', include('post_app.urls')),
    path('api/v1/', include('subscription_app.urls')),

]
