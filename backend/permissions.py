from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnerProfileOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user==request.user


class IsMasterOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool((request.user and request.user.is_staff and request.user.is_authenticated) or 
                    (request.user and request.user.is_superuser and request.user.is_authenticated))

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser and request.user.is_authenticated)


class IsAdminAndOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser and request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        if obj.id != request.user.id:
            return True
        return False
    


