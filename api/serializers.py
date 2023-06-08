from rest_framework import serializers

from .models import Services


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
