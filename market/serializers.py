from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=99)
    type = serializers.CharField(max_length=99)
    img = serializers.ImageField()
    price = serializers.DecimalField(max_digits=19, decimal_places=2)
    count = serializers.IntegerField()

class BuySerializer(serializers.Serializer):
    summary = serializers.IntegerField()

class ErrorMessage(serializers.Serializer):
    status = serializers.CharField(max_length=99)
    msg = serializers.CharField(max_length=99)
    reason = serializers.CharField(max_length=99)

class Hidden(serializers.Serializer):
    input = serializers.CharField(max_length=99)