from rest_framework import serializers

from apps.contacts.models import Contact
from common.utils import (
    format_phone_number,
    remove_none_values
)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "id", "name", "phone_number", "email", "company",
            "position", "address", "date_of_birth", "notes"
        )

    def to_representation(self, instance):
        result = super().to_representation(instance)
        formatted_phone_number = format_phone_number(instance.phone_number)
        if formatted_phone_number:
            result["phone_number"] = formatted_phone_number
        return remove_none_values(result)
