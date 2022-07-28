from rest_framework.routers import DefaultRouter

from app.views import UserViewSet, CustomerViewSet, DeviceViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'device', DeviceViewSet)

urlpatterns = []
urlpatterns += router.urls
