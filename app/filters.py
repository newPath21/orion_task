import django_filters

from app.models import Customer, Device


class CustomerFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='user__username', method='filter_username')
    email = django_filters.CharFilter(field_name='email', method='filter_email')

    class Meta:
        model = Customer
        fields = (
            'description',
        )

    def filter_username(self, queryset, name, value):
        query = queryset.filter(user__username=value)
        if query.exists():
            return query
        return queryset

    def filter_email(self, queryset, name, value):
        query = queryset.filter(user__email=value)
        if query.exists():
            return query
        return queryset


class DeviceFilter(django_filters.FilterSet):

    class Meta:
        model = Device
        fields = (
            'uuid',
            'dev_eui',
            'owner'
        )
