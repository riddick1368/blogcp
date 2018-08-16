from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
# Create your views here.



def product_detail_view(request,id):
    product = get_object_or_404(Product,id=id)
    context = {
        "product": product
    }
    template_name = "product_detail_view.html"
    return render(request,template_name,context)




def product_list_view(request):
    product = Product.objects.all()
    context = {
        "product":product
    }
    template_name = "product_list_view.html"
    return render(request, template_name, context)






