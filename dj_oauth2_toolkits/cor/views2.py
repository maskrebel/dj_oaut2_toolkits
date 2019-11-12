from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
    # def coba(self):
    #     return HttpResponse('OK')
    #
    # def contoh(self):
    #     return HttpResponse('ini contoh')