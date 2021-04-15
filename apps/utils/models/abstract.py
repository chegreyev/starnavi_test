import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractUUID(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name=_('uuid')
    )

    class Meta:
        abstract = True
        ordering = ('uuid',)


class AbstractTimeTrackable(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата изменения')
    )

    class Meta:
        abstract = True
        ordering = ('created_at', 'updated_at')


class AbstractCreatedBy(models.Model):
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
