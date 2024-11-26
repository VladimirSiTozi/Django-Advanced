from rest_framework.permissions import BasePermission


class IsBookOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        authors_name = obj.authors.values_list('name', flat=True)

        return request.user.username in authors_name