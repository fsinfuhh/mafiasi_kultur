from typing import List
from uuid import UUID

from django.db.models import Sum
from rest_framework.serializers import (
    IntegerField,
    ModelSerializer,
    Serializer,
    SerializerMethodField,
)

from mafiasi_kultur.core import models


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.MafiasiUser
        fields = ["id", "username"]


class AGSerializer(ModelSerializer):
    class Meta:
        model = models.AG
        fields = ["id", "name", "open_proposals", "viewings"]

    open_proposals = SerializerMethodField()
    viewings = SerializerMethodField()

    def get_open_proposals(self, obj: models.AG) -> List[UUID]:
        return [i.id for i in obj.mediums.exclude(proposal=None).filter(viewing=None)]

    def get_viewings(self, obj: models.AG) -> List[UUID]:
        return [i.id for i in obj.mediums.exclude(viewing=None)]


class ProposalSerializer(ModelSerializer):
    class Meta:
        model = models.Proposal
        fields = ["note", "proposed_by", "votes_cast", "vote_score"]

    proposed_by = SerializerMethodField()
    votes_cast = SerializerMethodField()
    vote_score = SerializerMethodField()

    def get_proposed_by(self, obj: models.Proposal) -> str:
        return obj.proposed_by.username

    def get_votes_cast(self, obj: models.Proposal) -> int:
        return obj.votes.count()

    def get_vote_score(self, obj: models.Proposal) -> int:
        return models.Vote.objects.filter(proposal=obj).aggregate(score=Sum("value", default=0))["score"]


class ViewingSerializer(ModelSerializer):
    class Meta:
        model = models.Viewing
        fields = ["viewed_at", "note"]


class MediumViewset(ModelSerializer):
    class Meta:
        model = models.Medium
        fields = ["id", "ag", "name", "proposal", "viewing"]

    proposal = ProposalSerializer()
    viewing = ViewingSerializer()


class CastVoteSerializer(Serializer):
    value = IntegerField(min_value=-1, max_value=1)
