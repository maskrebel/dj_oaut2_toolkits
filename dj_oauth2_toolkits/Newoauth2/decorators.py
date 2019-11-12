from __future__ import absolute_import

from functools import wraps
from urllib.parse import unquote_plus, urlparse, parse_qs, urlencode

from django.http import HttpResponseRedirect
from django.http import QueryDict
from django.http.response import Http404
from django.urls import reverse
from django.utils.decorators import available_attrs
from oauth2_provider.models import AccessToken
is_app = False
def login_required(is_staff=None):
    def real_decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def wrap(request, *args, **kwargs):
            if request.is_app and 'accessToken' in request.GET:
                try:
                    access_token = AccessToken.objects.get(token=request.GET['accessToken'])
                except AccessToken.DoesNotExist:
                    pass
                else:
                    request.user = access_token.user

            """ User telah terauthentikasi """
            if request.user and request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                query_dict = QueryDict(mutable=True)
                query_dict.update(request.GET)
                if is_staff:
                    query_dict.update({'staff': 1})
                query_string = urlencode(query_dict)
                return HttpResponseRedirect('{url}?{qs}'.format(url=reverse('auth:login'), qs=query_string))
        return wrap
    return real_decorator