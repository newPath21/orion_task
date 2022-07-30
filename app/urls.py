from rest_framework.routers import DefaultRouter
from django.urls import path

from app.views import CustomerRegisterView, DeviceViewSet, UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'device', DeviceViewSet)


urlpatterns = [
    path('customer_register', CustomerRegisterView.as_view()),
]

urlpatterns += router.urls
