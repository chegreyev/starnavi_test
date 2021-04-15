from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.const import LikeTypeChoice
from utils.models import AbstractUUID, AbstractTimeTrackable, AbstractCreatedBy


class Like(
    AbstractUUID,
    AbstractCreatedBy,
    AbstractTimeTrackable,
):

    type = models.CharField(
        max_length=7,
        choices=LikeTypeChoice.choices(),
    )

    class Meta:
        verbose_name = _("Лайк/Дизлайк")
        verbose_name_plural = _("Лайки/Дизлайки")

    def __str__(self):
        return f'{self.created_by.first_name} - {self.type}'
