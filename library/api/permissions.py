from rest_framework.permissions import SAFE_METHODS, BasePermission

from core.constants import Errors


class IsRenterReadOnly(BasePermission):
    """Пермишен, не позволяющий сдать книгу из аренды, если
    пользователь изначально не брал её в аренду."""

    message = Errors.ACTION_NOT_PERMITTED.value

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.reader == request.user
