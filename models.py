from django.db import models


class Product(models.Model):
    brand = models.CharField(max_length=100)
    product_description = models.CharField(max_length=200)
    is_manufacturer = models.BooleanField(default=False)
    productid = models.CharField(max_length=100)
    brandid = models.CharField(max_length=100)
    ecolabel = models.CharField(max_length=100)
    ecolabel_informations = models.CharField(max_length=500)
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)

    def __str__(self):
        return self.brand + " " + self.productid
