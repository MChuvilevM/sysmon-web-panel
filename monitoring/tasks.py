from celery import shared_task
from django.utils import timezone
from .models import Host, SystemMetric

@shared_task
def cleanup_old_metrics():
    threshold = timezone.now() - timezone.timedelta(days=30)
    deleted_count, _ = SystemMetric.objects.filter(timestamp__lt=threshold).delete()
    return f"Deleted {deleted_count} old metric records."
