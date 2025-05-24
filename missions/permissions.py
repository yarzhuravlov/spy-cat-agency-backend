from rest_framework import permissions

from missions.models import Mission


class DeleteIfIsUnassigned(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Mission):
        if view.action == "destroy":
            return not obj.cat

        return True
