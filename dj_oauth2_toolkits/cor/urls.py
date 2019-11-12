from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings
# from .views import ApiEndpoint
from django.urls import path
from . import views
from . import views2 as ApiEndpoint
from django.contrib.auth import views as auth_views
# OAuth2 provider endpoints
oauth2_endpoint_views = [
    # path('contoh/', ApiEndpoint, name="contoh")
]

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout/',views.logout_view, name='logout'),
    path('login_action/',views.login_action, name='login_action'),
    # path('api/hello', ApiEndpoint, name='api_point')
    # path('o/', include(oauth2_endpoint_views, name="oauth2_provider")),
    # path('api/hello', ApiEndpoint.as_view, name='api_point')
]
