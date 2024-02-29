from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerOauthRedirectView,
    SpectacularSwaggerView,
)
from rest_framework.routers import SimpleRouter

from mafiasi_kultur.api import viewsets

router = SimpleRouter()
router.register("ags", viewsets.AGViewset, basename="ag")
router.register("mediums", viewsets.MediumViewset, basename="medium")

urlpatterns = [
    path("schema.yml", SpectacularAPIView.as_view(), name="openapi_schema"),
    path("swagger-ui/", SpectacularSwaggerView.as_view(url_name="openapi_schema"), name="swagger_ui"),
    path("swagger-ui/oauth2-redirect.html", SpectacularSwaggerOauthRedirectView.as_view()),
    path("", include(router.urls)),
]
