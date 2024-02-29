import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class MafiasiUser(AbstractUser):
    """
    Custom Mafiasi User Model.
    It is not really used right now but since it is best practice to use one we have it.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class AG(models.Model):
    """
    The AG for which everything is scoped
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} AG"


class Medium(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ag = models.ForeignKey(to="AG", on_delete=models.PROTECT, related_name="mediums")
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Proposal(models.Model):
    """
    A proposal for a new media that the AG wishes to consume
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    medium = models.OneToOneField(to="Medium", on_delete=models.CASCADE)
    note = models.TextField()
    proposed_by = models.ForeignKey(to="MafiasiUser", on_delete=models.PROTECT, related_name="proposals")
    votes = models.ManyToManyField(to="MafiasiUser", through="Vote", through_fields=("proposal", "user"))

    def __str__(self):
        return self.medium.name


class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    proposal = models.ForeignKey(to="Proposal", on_delete=models.CASCADE)
    user = models.ForeignKey(to="MafiasiUser", on_delete=models.CASCADE)
    value = models.IntegerField(
        choices=[
            (-1, "dislike"),
            (0, "don't care"),
            (+1, "like"),
        ]
    )


class Viewing(models.Model):
    """
    A viewing of a certain medium
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    medium = models.OneToOneField(to="Medium", on_delete=models.CASCADE)
    viewed_at = models.DateTimeField()
    note = models.TextField()

    def __str__(self):
        return self.medium.name
