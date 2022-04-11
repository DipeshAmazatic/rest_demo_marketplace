from rest_framework import permissions
class ProductPermission(permissions.BasePermission):
    """
    Add new permission
    """
    def has_permission(self, request, view):
        
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated or request.user.is_staff or request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        print("object permission : ",view.action,request,obj,permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            # The method is a safe method
            return True
        else:
            # Only owners and superuser are granted permissions
            return obj.user == request.user or request.user.is_superuser
    