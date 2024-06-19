from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
    
# logic = if req. method is GET then only API will accessible i.e TRUE,   otherwise its denied.