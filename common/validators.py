import phonenumbers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(phone_number: str) -> None:
    exp = ValidationError(
        _("Please enter a valid phone number")
    )
    try:
        raw_phone_number = phonenumbers.parse(phone_number)
    except phonenumbers.NumberParseException:
        raise exp
    if not phonenumbers.is_valid_number(raw_phone_number):
        raise exp
