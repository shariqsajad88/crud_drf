from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Address, PhoneNumber
from .serializers import UserSerializer, AddressSerializer, PhoneNumberSerializer
from django.db.models import Count, Q

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.annotate(
        verified_phone_numbers_count=Count('phone_numbers', filter=Q(phone_numbers__is_verified=True), distinct=True),
        total_phone_numbers_count=Count('phone_numbers', distinct=True),
        verified_addresses_count=Count('addresses', filter=Q(addresses__is_verified=True), distinct=True),
        total_addresses_count=Count('addresses', distinct=True)
    )
    serializer_class = UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
