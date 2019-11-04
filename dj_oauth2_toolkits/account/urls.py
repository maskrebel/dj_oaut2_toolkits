from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'ac'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.do_login, name='login'),
    # path('loginaksi/', views.loginaksi, name='loginaksi'),
    # path('login/', views.login, name='login'),
    # # path('home/', views.home, name='home'),
    # path('settlement_marchant/', views.settlement_marchant, name='settlement_marchant'),
    # path('logout/', views.logout_view, name='logout'),
    # path('coba/', views.coba, name='coba'),
    # path('auth/callback/', views.auth_callback, name='auth_callback'),
]
