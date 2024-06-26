from typing import Union

import phonenumbers
from phonenumbers import PhoneNumber

T = Union[list, set, dict, tuple]


def parse_phone_number(phone_number: str) -> PhoneNumber | None:
    try:
        raw_phone_number = phonenumbers.parse(phone_number)
    except phonenumbers.NumberParseException:
        return
    return raw_phone_number


def format_phone_number(phone_number: str) -> str | None:
    raw_phone_number = parse_phone_number(phone_number)
    if raw_phone_number is None:
        return raw_phone_number
    formatted_phone_number = phonenumbers.format_number(raw_phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    return formatted_phone_number


def remove_none_values(values: T) -> list | dict:
    if isinstance(values, dict):
        return {k: v for k, v in values.items() if v is not None}
    return list(filter(lambda x: x is not None, values))
