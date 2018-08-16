from django.contrib import admin
from .models import Car,Brand,Product,Varation,Productimage
# Register your models here.




admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Varation)
admin.site.register(Productimage)

