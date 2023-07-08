from rest_framework import serializers
from .models import FunnelStatus, Customer, CustomerLog


class FunnelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunnelStatus
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLog
        fields = '__all__'
