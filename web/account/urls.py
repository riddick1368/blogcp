
from django.contrib import admin
from django.urls import path,include,re_path
from . import views





app_name="account"

urlpatterns = [
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),
    path('profile/',views.ViewProfile,name = "profile"),
    re_path(r'^profile/change/(?P<username>[a-zA-Z0-9]+)$',views.EditProfile,name='edit_profile'),
    re_path(r'^profile/change-password/(?P<username>[a-zA-Z0-9]+)/$', views.change_password, name='change_password'),
    path('contact/',views.contact,name="contact")
    ]
