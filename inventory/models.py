from django.db import models

# Create your models here.

class Supplier(models.Model):
    supplierid = models.CharField(max_length=8, primary_key=True)
    suppliername = models.TextField()
    supplieremail = models.TextField()
    supplierphonenum = models.CharField(max_length=12)
    supplieraddress = models.CharField(max_length=100)

    def __str__(self):
        return self.supplierid

class Product(models.Model):
    productid = models.CharField(max_length = 8, primary_key = True)
    productname = models.TextField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    productqty = models.IntegerField()
    productprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.productname

    @property
    def supplier_name(self):
        return self.supplier.suppliername

class Receiver(models.Model):
    receiverid = models.AutoField(primary_key=True)
    receivername = models.TextField()
    receiverpositions = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    receiveqty = models.IntegerField()
    receivedate = models.DateField()
    receivestatus = models.CharField(max_length=100)

    @property
    def product_name(self):
        return self.product.productname