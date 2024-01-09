from rest_framework.permissions import BasePermission


class OnlyGetPublic(BasePermission):
    def has_permission(self,request,view):
        if request.method != "GET":
            return request.user.is_authenticated
        
        return True