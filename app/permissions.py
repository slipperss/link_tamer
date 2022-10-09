from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReadOnly(BasePermission):
    #  Доступ не авторизированным юзерам к безопасным методам не включая {'get': 'list'}
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and
            view.action == 'retrieve'
        )


class IsAuthenticated(BasePermission):
    #  Доступ для авторизированных пользователей
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated
        )


class IsLinkOwnerOrAdminOrRetrieve(BasePermission):
    #  Доступ к обьекту для владельцев и админов, + доступ любым юзерам к  {'get': 'retrieve'}
    def has_object_permission(self, request, view, obj):
        return bool(
            obj.owner == request.user or
            request.user and request.user.is_staff or
            view.action == 'retrieve'
        )
