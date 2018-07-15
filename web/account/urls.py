
from django.contrib import admin
from django.urls import path,include,re_path
from . import views





app_name="account"

urlpatterns = [
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),
 ]
