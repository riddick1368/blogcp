from django.contrib import admin
from .models import Car,Brand,Product,Varation,Productimage
# Register your models here.

class ProductCustomise(admin.ModelAdmin):
    list_display = ["title","car"]


admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Product,ProductCustomise)
admin.site.register(Varation)
admin.site.register(Productimage)

