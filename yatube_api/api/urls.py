from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet, GroupViewSet

app_name = 'api'


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
urlpatterns = [
    path('api/v1/api-token-auth/', obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
