from rest_framework import serializers
from .models import Client, Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'start_date', 'end_date', 'status']

class ClientSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'email', 'phone', 'is_active', 'subscriptions']
