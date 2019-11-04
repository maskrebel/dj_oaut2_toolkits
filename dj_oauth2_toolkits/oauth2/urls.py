from django.urls import path, include
from . import views

# app_name = 'o'
urlpatterns = [
    path('', views.do_login, name='login'),

    ]