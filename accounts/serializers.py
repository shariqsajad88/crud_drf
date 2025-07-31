from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address, PhoneNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id', 'user', 'number', 'is_verified']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'user' ,'address_line', 'city', 'postal_code', 'is_verified']

class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)
    verified_phone_numbers_count = serializers.SerializerMethodField()
    verified_addresses_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'addresses',
            'phone_numbers',
            'verified_phone_numbers_count',
            'verified_addresses_count'
        ]

    def get_verified_phone_numbers_count(self, obj):
        return obj.phone_numbers.filter(is_verified=True).count()

    def get_verified_addresses_count(self, obj):
        return obj.addresses.filter(is_verified=True).count()
