from django.db import models

# Create your models here.

class Supplier(models.Model):
    supplierid = models.CharField(max_length=8, primary_key=True)
    suppliername = models.TextField()
    supplieremail = models.TextField()
    supplierphonenum = models.CharField(max_length=12)
    supplieraddress = models.CharField(max_length=100)

    def __str__(self):
        return self.suppliername

class Product(models.Model):
    productid = models.CharField(max_length = 8, primary_key = True)
    productname = models.TextField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    productqty = models.PositiveIntegerField(default=0)
    productprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.productid

    def substract_quantity(self, quantity):
        quantity = int(quantity) # convert quantity to an integer
        self.productqty -= quantity

        if self.productqty < 0:
            self.productqty = 0

        self.save()

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

    def save(self, *args, **kwargs):
        # call the superclass's save() method to save the Receiver instance
        super().save(*args, **kwargs)

        # substract the received quantity from the product quantity
        self.product.substract_quantity(self.receiveqty)

    @property
    def product_name(self):
        return self.product.productid