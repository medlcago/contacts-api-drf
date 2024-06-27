from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "email", "password",
            "date_joined", "is_active", "is_staff"
        )
        extra_kwargs = {
            "date_joined": {"read_only": True},
            "is_active": {"read_only": True},
            "is_staff": {"read_only": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data) -> User:
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data) -> User:
        if "password" in validated_data:
            raise serializers.ValidationError(
                detail={
                    "detail": "You cannot update the password field."
                }
            )
        return super().update(instance, validated_data)
