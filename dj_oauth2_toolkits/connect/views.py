# from django.shortcuts import render, redirect
# from django.urls import reverse
# from .forms import LoginForm
# from django.core.exceptions import MultipleObjectsReturned
# from django.contrib.auth import login, authenticate
# from django.http import HttpResponseRedirect, HttpResponse
# from urllib.parse import parse_qs, urlencode, urlparse, urlunparse
# from django.contrib.auth import logout
#
# # from django.views.decorators.csrf import csrf_protect, requires_csrf_token
# # from oauth2.decorators import calculate_redirect_to
#
# INCORRECT_CREDENTIAL_MSG = 'Username/email atau password yang Anda masukan salah'
#
# # @calculate_redirect_to
# # def do_login(request):
# #
# #     def add_query_string(old_url, qs):
# #         add_qs = parse_qs(qs)
# #         parse_list = list(urlparse(old_url))
# #         new_qs = parse_qs(parse_list[4])
# #         new_qs.update(add_qs)
# #         parse_list[4] = urlencode(new_qs, doseq=True)
# #         return urlunparse(parse_list)
# #
# #     def select_template_url(request, data, client_id, query_string, error_msg=''):
# #         template = render(request, 'login.html', data)
# #         # if request.is_app is True and request.GET.get('from') == 'google':
# #         #     template = HttpResponseRedirect(add_query_string(reverse('auth:google_login'), query_string))
# #         #     template.set_cookie('errorMsg', error_msg, max_age=30)
# #
# #         return template
# #
# #     query_string = urlencode(request.GET)
# #
# #     client_id = request.GET.get('clientId')
# #     is_adult = request.GET.get('adult', 0)
# #     redirect_to = request.session.get('redirect_to')
# #     data = {
# #         'query_string': query_string,
# #         'form': LoginForm() if request.method == 'GET' else LoginForm(request.POST) if request.method == 'POST' else None,
# #     }
# #     # if client_id:
# #     #     try:
# #     #         client_details = AppsClient.objects.get(id=client_id)
# #     #     except AppsClient.DoesNotExist:
# #     #         return render(request, 'detikconnect/dc/desktop/404.html', data)
# #     #     data['back_url'] = client_details.site_url if client_details.site_url else client_details.base_domain
# #     #     data['app_name'] = settings.CUSTOM_TEMPLATE_CLIENT.get(client_id, None)
# #     # else:
# #     #     client_details = None
# #
# #     query_string = urlencode(request.GET)
# #     if request.method == 'POST':
# #
# #         """ INIT Form POST Request """
# #         form = data['form']
# #         form_valid = form.is_valid()
# #
# #         if form_valid:
# #             cleaned_data = form.cleaned_data
# #             username = cleaned_data['username']
# #             password = cleaned_data['password']
# #
# #             username = username.lower()
# #
# #             try:
# #                 user = authenticate(username=username, password=password)
# #             except MultipleObjectsReturned:
# #                 request.session['duplicate_email'] = username
# #                 return HttpResponseRedirect(add_query_string(reverse('auth:choose_user'), query_string))
# #
# #             if user is None:
# #                 data['errorMsg'] = INCORRECT_CREDENTIAL_MSG
# #                 return select_template_url(request, data, client_id, query_string, data['errorMsg'])
# #             else:
# #                 return redirect('/o/dashboard')
# #
# #     return select_template_url(request, data, client_id, query_string, data.get('errorMsg', None))
# class login:
#     def do_login(request):
#         template = render(request, 'login.html')
#         return template
#
#     def dashboard(request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             responese = HttpResponse('sudah login <a href="../logout"> Log Out<a>')
#         else:
#         # if request.user.is_authenticated:
#         #
#         #     response = HttpResponse('sudah login <a href="../logout"> Log Out<a>')
#         # else:
#             response = HttpResponse('<a href="../logout"> Log Out<a>')
#         return response
#
#     def logout_view(request):
#         logout(request)
#         return redirect('../')


from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

