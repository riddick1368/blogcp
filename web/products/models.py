from django.db import models

# Create your models here.





class Car (models.Model):
    title = models.CharField(max_length=120)
    year = models.IntegerField(default=None)



    def __str__(self):
        return self.title

class Brand (models.Model):
    title = models.CharField(max_length=120)


    def __str__(self):
        return self.title



class Product (models.Model):
    brand = models.ManyToManyField(Brand)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=20,decimal_places=2,default=None)
    active = models.BooleanField(default=True)



    def __str__(self):
        return self.title


class Varation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2,blank=True,null=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title



    def get_sale_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

class Productimage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField()



    def __str__(self):
        return self.product.title