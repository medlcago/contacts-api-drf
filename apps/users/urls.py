from django.urls import path, include
from rest_framework import routers

from apps.users.views import UserModelViewSet

router = routers.DefaultRouter()
router.register(r"users", UserModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
