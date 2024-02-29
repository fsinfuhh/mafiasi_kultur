import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class MafiasiUser(AbstractUser):
    """
    Custom Mafiasi User Model.
    It is not really used right now but since it is best practice to use one we have it.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
