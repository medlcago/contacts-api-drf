from rest_framework.permissions import IsAuthenticated


class IsOwnerOrCreateOnly(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method == "POST"

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
