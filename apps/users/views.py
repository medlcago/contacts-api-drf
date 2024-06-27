from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users.permissions import IsOwnerOrCreateOnly
from apps.users.serializers import UserSerializer

User = get_user_model()


class UserModelViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrCreateOnly,)

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)
