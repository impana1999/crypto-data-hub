from rest_framework import serializers
from .models import Organization, CryptoPrice

class OrganizationSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')  

    class Meta:
        model = Organization
        fields = '__all__'


class CryptoPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoPrice
        fields = '__all__'
