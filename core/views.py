from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Client, Subscription
from .serializers import ClientSerializer, SubscriptionSerializer
from django.shortcuts import get_object_or_404
from datetime import date

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        client = self.get_object()
        client.is_active = True
        client.save()
        return Response({'status': 'client activated'})

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        client = self.get_object()
        client.is_active = False
        client.save()
        return Response({'status': 'client deactivated'})

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all().order_by('id')
    serializer_class = SubscriptionSerializer

    @action(detail=False, methods=['get'])
    def expiring_soon(self, request):
        today = date.today()
        soon = today.replace(day=today.day)  # keep simple
        # Example: find subscriptions ending in next 7 days
        from datetime import timedelta
        limit = today + timedelta(days=7)
        subs = Subscription.objects.filter(end_date__lte=limit, end_date__gte=today)
        serializer = self.get_serializer(subs, many=True)
        return Response(serializer.data)
