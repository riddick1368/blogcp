
from django.contrib import admin
from django.urls import path,include,re_path







app_name="polls"

urlpatterns = [
    path('admin/', admin.site.urls),

]