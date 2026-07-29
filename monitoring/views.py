from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Host, SystemMetric
from .serializers import HostSerializer, SystemMetricSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class SystemMetricViewSet(viewsets.ModelViewSet):
    queryset = SystemMetric.objects.all()
    serializer_class = SystemMetricSerializer

@api_view(['GET', 'POST'])
def api_metrics(request):
    if request.method == 'POST':
        serializer = SystemMetricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    metrics = SystemMetric.objects.all()
    serializer = SystemMetricSerializer(metrics, many=True)
    return Response(serializer.data)
