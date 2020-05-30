from rest_framework import permissions


class TokenPermission(permissions.BasePermission):
    message = 'You must be authenticated to perform this action'

    def has_permission(self, request, view):
        return request.auth is not None
