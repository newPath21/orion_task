from uuid import uuid4
from django.utils.translation import ugettext_lazy as _

from django.db import models


class AbstractUUID(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
        verbose_name=_('uuid')
    )

    class Meta:
        abstract = True
        ordering = ('uuid',)
