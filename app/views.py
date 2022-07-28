from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth.models import User

from app.filters import CustomerFilter, DeviceFilter
from app.models import Customer, Device
from app.serializers import CustomerSerializer, CustomerCreateSerializer, UserSerializer, DeviceSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        serializer_class = CustomerSerializer

        if self.action == 'create':
            serializer_class = CustomerCreateSerializer

        return serializer_class


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filterset_class = DeviceFilter
    permission_classes = [IsAuthenticated,]
