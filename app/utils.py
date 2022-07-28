from enum import Enum


class Choice(Enum):
    @classmethod
    def choices(cls):
        return [(c.value, c.name) for c in cls]


class DeviceType(str, Choice):
    TYPE1 = 'TYPE1'
    TYPE2 = 'TYPE2'
