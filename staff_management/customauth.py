from rest_framework.authentication import BaseAuthentication


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get()