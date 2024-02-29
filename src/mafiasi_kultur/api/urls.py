from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from mafiasi_kultur.api import viewsets

router = SimpleRouter()

urlpatterns = [
    path("schema.yml", SpectacularAPIView.as_view(), name="openapi_schema"),
    path("swagger-ui/", SpectacularSwaggerView.as_view(url_name="openapi_schema"), name="swagger_ui"),
    path("", include(router.urls)),
]
