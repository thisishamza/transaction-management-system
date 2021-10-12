from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()

class AuditFieldMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(user, verbose_name="created by", on_delete=models.PROTECT,
                                   related_name="created_%(app_label)s_%(class)s_set")
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(user, verbose_name="modified by", on_delete=models.PROTECT,
                                    related_name="modified_%(app_label)s_%(class)s_set")

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
