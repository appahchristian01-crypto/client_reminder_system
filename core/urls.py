from rest_framework import routers
from .views import ClientViewSet, SubscriptionViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
