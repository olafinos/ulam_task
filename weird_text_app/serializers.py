from rest_framework import serializers

class EncodeSerializer(serializers.Serializer):
    text = serializers.CharField(trim_whitespace=False)

class DecodeSerializer(serializers.Serializer):
    text = serializers.CharField(trim_whitespace=False)