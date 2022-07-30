import csv

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from app.filters import DeviceFilter
from app.models import Customer, Device
from app.serializers import CustomerSerializer, DeviceSerializer, \
    DeviceCSVSerializer, UserSerializer, SuccessSerializer
from django.contrib.auth.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filterset_class = DeviceFilter
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated,]

    def get_serializer_class(self):
        serializer_class = DeviceSerializer

        if self.action == 'create_csv':
            serializer_class = DeviceCSVSerializer
        return serializer_class

    @action(methods=['POST'], detail=True, url_path='create_csv')  # reading from device into csv
    def create_csv(self, request, *args, **kwargs):
        device_id = kwargs.get('pk')
        device = Device.objects.get(uuid=device_id)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=f"{device.uuid}.csv"'
        writer = csv.writer(response)
        writer.writerow(['type', 'description'])
        writer.writerow([device.type, device.description])
        return response


class CustomerRegisterView(GenericAPIView):
    @swagger_auto_schema(
        request_body=CustomerSerializer(),
        responses={201: SuccessSerializer()}
    )
    def post(self, request):
        obj = Customer.objects.get_or_create(user=self.request.user)
        serializer = CustomerSerializer(obj, request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'success': True})
