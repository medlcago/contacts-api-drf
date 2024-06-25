import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_phone_number(phone_number):
    pattern = re.compile(r"^\+\d{8,15}$")
    if not pattern.match(phone_number):
        raise ValidationError(
            _("Please enter a valid phone number"),
        )
