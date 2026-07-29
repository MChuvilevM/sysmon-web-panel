from django.contrib import admin
from .models import Host, SystemMetric

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'ip_address')

@admin.register(SystemMetric)
class SystemMetricAdmin(admin.ModelAdmin):
    list_display = ('host', 'cpu_usage', 'memory_usage', 'disk_usage', 'timestamp')
    list_filter = ('host', 'timestamp')
    search_fields = ('host__name', 'host__ip_address')
