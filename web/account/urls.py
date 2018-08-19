
from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.contrib.auth.views import password_reset,password_reset_done





app_name="account"

urlpatterns = [
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),
    path('profile/',views.ViewProfile,name = "profile"),
    re_path(r'^profile/change/(?P<username>[a-zA-Z0-9]+)$',views.EditProfile,name='edit_profile'),
    re_path(r'^profile/change-password/(?P<username>[a-zA-Z0-9]+)/$', views.change_password, name='change_password'),
    path('contact/',views.contact,name="contact"),
    re_path(r'^reset-password/$',password_reset,name='rest_password'),
    re_path(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
    ]
