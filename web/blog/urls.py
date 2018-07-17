
from django.urls import path,include,re_path
from . import views





app_name="blog"

urlpatterns = [
    path('post-list',views.Post_list,name="post_list"),
    path('post-create',views.Post_create,name="post_create"),
    re_path(r'^delete/(?P<id>\d+)/$',views.post_delete,name="post_delete"),
    re_path(r'^(?P<id>\d+)/$',views.Post_detail,name="post-single"),
    re_path(r'^edit/(?P<id>\d+)/$',views.post_edit,name="post_edit")
]



