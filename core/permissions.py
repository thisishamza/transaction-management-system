from rest_framework.permissions import BasePermission
from users.models import UserTypeChoices


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user.type == UserTypeChoices.CUSTOMER:
            return True
