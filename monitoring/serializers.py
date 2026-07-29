from rest_framework import serializers
from .models import Host, SystemMetric

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

class SystemMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMetric
        fields = '__all__'
