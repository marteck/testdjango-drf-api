from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsStaffUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.is_superuser)


class IsOwner(permissions.BasePermission):  # Ticket creator or admin can PUT Ticket

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser or request.user.is_staff:
                return True
            else:
                return obj.user == request.user
        else:
            return False


class IsAuthor(permissions.BasePermission):  # The answer is only for ticket owner and only for GET

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser or request.user.is_staff:
                return True
            else:
                return obj.ticket_id.user == request.user
        else:
            return False



