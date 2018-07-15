
from django.contrib import admin
from django.urls import path,include,re_path





app_name="blog"

urlpatterns = [
    path('admin/', admin.site.urls),
]



