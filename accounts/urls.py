from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AddressViewSet, PhoneNumberViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'phone-numbers', PhoneNumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
