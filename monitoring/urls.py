from django.urls import path
from .views import api_metrics

urlpatterns = [
    path('metrics/', api_metrics, name='api_metrics'),
]
