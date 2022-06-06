from rest_framework import serializers


class SignInSerialize(serializers.Serializer):
    login = serializers.CharField(max_length=99)
    password = serializers.CharField(max_length=99)
