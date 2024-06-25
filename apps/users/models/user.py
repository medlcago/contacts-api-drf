from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, *, email: str, password: str, **extra_fields) -> "User":
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, *, email: str, password: str, **extra_fields) -> "User":
        extra_fields["is_superuser"] = False
        return self._create_user(
            email=email,
            password=password,
            **extra_fields
        )

    def create_superuser(self, *, email: str, password: str, **extra_fields) -> "User":
        extra_fields["is_superuser"] = True
        extra_fields["is_staff"] = True
        return self._create_user(
            email=email,
            password=password,
            **extra_fields
        )

    def create_admin(self, *, email: str, password: str, **extra_fields) -> "User":
        extra_fields["is_staff"] = True
        return self._create_user(
            email=email,
            password=password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    password = models.CharField(
        _("password"),
        max_length=128,
        validators=[
            MinLengthValidator(6),
        ])
    date_joined = models.DateTimeField(_("registered"), auto_now_add=True)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("id",)

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
