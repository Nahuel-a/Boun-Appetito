from rest_framework import serializers
from .models import Order, Pizza, Send


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("user", "price", "send", "payment_method", "created_ad")
        read_only_fields = (
            "user",
            "created_ad",
        )


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = (
            "order",
            "name",
            "description",
            "amount",
            "price",
            "image",
            "is_active",
        )
        read_only_fields = (
            "order",
            "is_active",
        )


class SendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Send
        fields = ("order", "address", "number", "description_extras", "price")
