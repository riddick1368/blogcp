
from django.contrib import admin
from django.urls import path,include,re_path
from . import views







app_name="polls"

urlpatterns = [
    path('poll-list/',views.Poll_list,name="poll_list"),
    re_path(r'^poll-list/(?P<id>\d+)/$',views.Poll_single,name="poll_single"),
    path('poll-list/create',views.Poll_create,name="poll_create"),
    re_path(r'^poll-list/delete/(?P<id>\d+)/$',views.Poll_delete,name="poll_delete"),
    re_path(r'^choice/choice-edit/(?P<id>\d+)/$',views.Choice_edit,name="choice_edit"),
    re_path(r'^choice/choice-create/(?P<id>\d+)/$',views.Choice_create,name="choice_create"),
    re_path(r'^choice/choice-delete/(?P<id>\d+)/$',views.choice_delete,name="choice_delete"),
    re_path(r'^poll-list/edit/(?P<id>\d+)/$',views.Poll_edit,name="poll_edit")


]