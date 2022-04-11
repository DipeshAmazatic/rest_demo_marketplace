from rest_framework import permissions

class CompanyPermission(permissions.BasePermission):
    """
    Add new permission
    """
    def has_permission(self, request, view):
        if view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff or request.user.is_superuser
        return request.user.is_authenticated