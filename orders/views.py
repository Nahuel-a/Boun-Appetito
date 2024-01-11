from rest_framework import viewsets

from .serializers import OrderSerializer, PizzaSerializer, SendSerializer
from .models import Order, Pizza, Send


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class SendViewSet(viewsets.ModelViewSet):
    queryset = Send.objects.all()
    serializer_class = SendSerializer
