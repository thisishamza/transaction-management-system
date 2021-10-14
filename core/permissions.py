from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import UserTypeChoices


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user.type == UserTypeChoices.CUSTOMER:
            return True


class IsAccountOwnerOrReadOnly(BasePermission):
    message = "You are not allowed to view this data."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and obj.user == request.user:
            return True


class IsTransactionOwnerOrReadOnly(BasePermission):
    message = "You are not allowed to view this data."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and obj.account.user == request.user:
            return True
