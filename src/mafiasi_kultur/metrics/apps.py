from django.apps import AppConfig
from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, Resource

from mafiasi_kultur import __version__ as app_version


class MetricsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mafiasi_kultur.metrics"
    label = "mafiasi_kultur_metrics"

    def ready(self):
        super().ready()
        self.init_instrumentation()

    def init_instrumentation(self):
        from mafiasi_kultur.metrics import async_instruments

        resource = Resource(
            attributes={
                SERVICE_NAME: "mafiasi_kultur",
                SERVICE_VERSION: app_version,
            }
        )
        metric_reader = PrometheusMetricReader()
        meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
        metrics.set_meter_provider(meter_provider)
        async_instruments.create_async_instruments()
