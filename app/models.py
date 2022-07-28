from geoposition.fields import GeopositionField

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from app.abstracts import AbstractUUID
from app.utils import DeviceType


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    description = models.TextField(
        _('описание'),
        max_length=500
    )

    def __str__(self):
        return f'Клиент {self.user.username}'


class Device(AbstractUUID):
    dev_eui = models.CharField(
        _("идентификатор по устройству"),
        max_length=50,
        unique=True,
        default='E544334343'
    )
    state = models.BooleanField(
        _('вкл/выкл'),
        default=False,
    )
    last_reading_time = models.DateTimeField(
        _('время последнего показания'),
        null=True
    )
    activation_time = models.DateTimeField(
        _('время активации'),
        null=True
    )
    description = models.TextField(
        _('описание')
    )
    type = models.CharField(
        _("тип устройства"),
        max_length=50,
        choices=DeviceType.choices(),
        default=DeviceType.TYPE1,
    )
    owner = models.ForeignKey(
        Customer,
        verbose_name= _('владелец'),
        on_delete=models.CASCADE,
        related_name='devices',
    )

    def __str__(self):
        return f'Устройства типа {self.type}'


class Meter(AbstractUUID):
    serial_number = models.CharField(
        _('номер на счетчике'),
        max_length=100)
    state = models.BooleanField(
        _('вкл/выкл'),
        default=False,
    )
    register_time = models.DateTimeField(
        _('время регистрации'),
        auto_now=True,
    )
    initial_reading_time = models.DateTimeField(
        _('время начального показания'),
        null=True
    )
    initial_value = models.FloatField(
        _('время первого показания'),
        default=0.0,
    )
    measurement_unit = models.CharField(
        _('единица измерения'),
        max_length=100
    )

    def __str__(self):
        return f'Номер на счетчике {self.serial_number}'


class Node(AbstractUUID):
    geo = GeopositionField()
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        _('описание'),
        blank=True
    )
    owner = models.ForeignKey(
        Customer,
        verbose_name=_('владелец'),
        related_name='nodes',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    address = models.TextField(
        max_length=100
    )

    def __str__(self):
        return f'Название узла {self.name}'
