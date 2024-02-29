from django.urls import path

from mafiasi_kultur.metrics import views

urlpatterns = [
    path("", views.PrometheusMetricsView.as_view(), name="prometheus_metrics"),
]
