import pytest
from django.shortcuts import resolve_url
from django.test import Client
from prometheus_client.parser import text_string_to_metric_families


@pytest.mark.django_db
def test_metric_endpoint_returns_valid_prometheus_data(client: Client):
    response = client.get(resolve_url("prometheus_metrics"))
    assert response.status_code == 200
    metrics = list(text_string_to_metric_families(response.content.decode("UTF-8")))
    assert len(metrics) > 0
