from django.conf import settings
from simple_openid_connect.integrations.django.user_mapping import FederatedUserData
from simple_openid_connect.integrations.django.user_mapping import (
    UserMapper as BaseUserMapper,
)

from mafiasi_kultur.core import models


class MafiasiUserMapper(BaseUserMapper):
    def automap_user_attrs(self, user: models.MafiasiUser, user_data: FederatedUserData) -> None:
        super().automap_user_attrs(user, user_data)

        if settings.OPENID_ANY_USER_IS_ADMIN:
            user.is_superuser = True
            user.is_staff = True

        elif hasattr(user_data, "groups") and isinstance(user_data.groups, list):
            if any(i_group in user_data.groups for i_group in settings.OPENID_SUPERUSER_GROUPS):
                user.is_superuser = True
                user.is_staff = True
