from rest_framework import viewsets
from .models import Host, SystemMetric
from .serializers import HostSerializer, SystemMetricSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class SystemMetricViewSet(viewsets.ModelViewSet):
    queryset = SystemMetric.objects.all()
    serializer_class = SystemMetricSerializer
