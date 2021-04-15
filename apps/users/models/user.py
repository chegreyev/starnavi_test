from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from users.manager import UserManager
from utils.models import AbstractUUID, AbstractTimeTrackable


class User(
    AbstractUUID,
    AbstractTimeTrackable,
    AbstractBaseUser,
    PermissionsMixin,
):

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
    )
    first_name = models.CharField(
        _('first name'),
        max_length=150,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
    )
    patronymic = models.CharField(
        _('patronymic'),
        max_length=150,
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        verbose_name=_("Аватар"),
        null=True,
        blank=True,
    )
    phone = models.CharField(
        _('phone'),
        max_length=15,
        blank=True,
        null=True,
    )
    last_activity = models.DateTimeField(
        _('last activity time'),
        blank=True,
        null=True,
    )
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'
