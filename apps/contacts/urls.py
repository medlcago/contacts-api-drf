from django.urls import path, include
from rest_framework import routers

from apps.contacts.views import ContactModelViewSet

router = routers.DefaultRouter()
router.register(r"contacts", ContactModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
