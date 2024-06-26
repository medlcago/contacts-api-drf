from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.validators import validate_phone_number

User = get_user_model()


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(_("name"), max_length=64, validators=[MinLengthValidator(1)])
    phone_number = models.CharField(_("phone number"), max_length=16, validators=[validate_phone_number])
    email = models.EmailField(_("email address"), max_length=64)
    company = models.CharField(_("company"), max_length=64, blank=True, null=True)
    position = models.CharField(_("position"), max_length=64, blank=True, null=True)
    address = models.CharField(_("address"), max_length=64, blank=True, null=True)
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    notes = models.CharField(_("notes"), max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.user} | Контакт {self.name}"

    class Meta:
        ordering = ("id",)
