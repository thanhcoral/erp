from turtle import position
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


USER_LEVEL_CHOICES = (
    ('SYSTEM_ADMIN', "System admin"),
    ('SUB_ADMIN', "Sub admin"),
    # (ACCOUNTANT, "Accountant"),
    # (AR_OFFICER, "AR Officer"),
    # (AP_OFFICER, "AP Officer"),
    # (PRODUCTION_MANAGER, "Production manager"),
    # (PURCHASE_MANAGER, "Purchase manager"),
    # (STOCK_MANAGER, "Stock manager"),
    # (SALE_MAN, "Sale man"),
    ('INQUIRIES', "Inquiries"),
)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[UnicodeUsernameValidator()],
        error_messages={"unique": _("A user with that username already exists."),},
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    position = models.CharField(_("position"), max_length=150, choices=USER_LEVEL_CHOICES, default='INQUIRIES', blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")