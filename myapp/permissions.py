from rest_framework import permissions

class IsOrgCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user  #  Only allow if user created the org
