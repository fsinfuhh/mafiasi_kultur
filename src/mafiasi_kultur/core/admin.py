from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

admin.site.login_template = "core/login.html"
admin.site.register(models.MafiasiUser, UserAdmin)
admin.site.register(models.AG)
admin.site.register(models.Medium)
admin.site.register(models.Proposal)
admin.site.register(models.Viewing)
admin.site.register(models.Vote)
