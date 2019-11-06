from functools import wraps
from django.utils.decorators import available_attrs
from django.urls import reverse
from django.http.response import Http404
# from detikconnect.common_functions import is_safe_url, delete_all_cookies

def calculate_redirect_to(view_func):
    @wraps(view_func, assigned=available_attrs(view_func))
    def wrap(request, *args, **kwargs):
        redirect_to = reverse('dashboard:dashboard')
        query_string = request.META['QUERY_STRING']
        redirect_to = "{}?{}".format(redirect_to, query_string)

        if request.GET.get('adult', '0') == '1':
            redirect_url = "{url}?{qs}".format(url=reverse('dashboard:dashboard-setting-birthday'), qs=query_string)
        else:
            redirect_url = request.GET.get('redirectUrl', None)

        if request.GET.get('clientId', '') != '':
            try:
                apps_detail = AppsClient.objects.get(id=request.GET['clientId'])
            except (AppsClient.DoesNotExist, AppsClient.MultipleObjectsReturned):
                raise Http404
            else:
                redirect_to = apps_detail.redirect_uris.split(',')[0] if apps_detail.redirect_uris else apps_detail.base_domain

        if redirect_url and is_safe_url(redirect_url):
            redirect_to = redirect_url
        request.session['redirect_to'] = redirect_to

        response = view_func(request, *args, **kwargs)
        return response

    return wrap