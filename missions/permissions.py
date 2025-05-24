from rest_framework import permissions

from missions.models import Mission


class DeleteIfIsUnassigned(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Mission):
        if view.action == "destroy":
            return not obj.cat

        return True


class IsCatAssignedToMission(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        mission = obj if isinstance(obj, Mission) else obj.mission

        return mission.cat == request.user


class IsTaskNotCompleted(permissions.BasePermission):
    def has_permission(self, request, view):
        target = view.get_object()
        return not target.is_completed
