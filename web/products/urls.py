from django.urls import path,include,re_path
from . import views




app_name ="products"



urlpatterns = [
    re_path(r'^list-product/(?P<id>\d+)/$',views.product_detail_view,name="product_detail_view"),
    path ('list-product/',views.product_list_view,name="prodtuc_list_view")

]