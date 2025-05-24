from rest_framework import serializers, permissions


class BaseViewSetMixin:
    """
    Mixin for mapping actions with serializers and permissions
    """

    def get_serializer_class(self) -> serializers.Serializer:
        if (
            hasattr(self, "action_serializers")
            and self.action in self.action_serializers
        ):
            return self.action_serializers[self.action]

        return super().get_serializer_class()

    def get_permissions(self) -> permissions.BasePermission:
        if (
            hasattr(self, "action_permissions")
            and self.action in self.action_permissions
        ):
            return [
                permission()
                for permission in self.action_permissions[self.action]
            ]

        return super().get_permissions()
