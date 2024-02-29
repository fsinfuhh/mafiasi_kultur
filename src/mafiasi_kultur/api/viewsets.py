from uuid import UUID

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, inline_serializer
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from mafiasi_kultur.api import serializers
from mafiasi_kultur.core import models


class AGViewset(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = models.AG.objects.all().prefetch_related("mediums", "mediums__proposal", "mediums__viewing")
    serializer_class = serializers.AGSerializer
    permission_classes = [IsAuthenticated]


class MediumViewset(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = models.Medium.objects.all()
    serializer_class = serializers.MediumViewset
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        if self.request.query_params.get("unvoted_only", "false") == "true":
            queryset = queryset.exclude(proposal__votes=self.request.user)
        if "ag" in self.request.query_params.keys():
            ag_id = UUID(hex=self.request.query_params["ag"])
            queryset = queryset.filter(ag_id=ag_id)

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter("ag", OpenApiTypes.UUID, OpenApiParameter.QUERY),
            OpenApiParameter("unvoted_only", OpenApiTypes.BOOL, OpenApiParameter.QUERY),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(request=serializers.CastVoteSerializer)
    @action(detail=True, methods=["post"])
    def cast_vote(self, request: Request, pk: UUID) -> Response:
        request_data = serializers.CastVoteSerializer(data=request.data)
        request_data.is_valid(raise_exception=True)

        instance = self.get_object()
        models.Vote.objects.update_or_create(
            proposal=instance.proposal,
            user=request.user,
            defaults={
                "value": request_data.validated_data["value"],
            },
        )
        instance.refresh_from_db()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
