from django.contrib import admin
from .models import PhoneNumber, Address

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'number', 'is_verified']
    list_filter = ['is_verified', 'user']
    search_fields = ['number', 'user__username']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address_line', 'city', 'postal_code', 'is_verified']
    list_filter = ['is_verified', 'city', 'user']
    search_fields = ['address_line', 'city', 'postal_code', 'user__username']
