from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.const import LikeTypeChoice
from utils.models import AbstractUUID, AbstractTimeTrackable, AbstractCreatedBy


class Post(
    AbstractUUID,
    AbstractCreatedBy,
    AbstractTimeTrackable,
):

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name of the Post"),
    )
    description = models.TextField(
        verbose_name=_("Description of the Post"),
        blank=True,
        null=True
    )
    likes = models.ManyToManyField(
        to="posts.Like",
        blank=True,
    )

    class Meta:
        verbose_name = _("Пост")
        verbose_name_plural = _("Посты")
        ordering = ''

    def __str__(self):
        return f'{self.name} - {self.likes_count} - {self.dislikes_count}'

    @property
    def likes_count(self):
        return self.likes.filter(type=LikeTypeChoice.LIKE.value).count()

    @property
    def dislikes_count(self):
        return self.likes.filter(type=LikeTypeChoice.DISLIKE.value).count()
