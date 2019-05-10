from django.db import models
from products.models import Product

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status of order'
        verbose_name_plural = 'Status of orders'


class Order(models.Model):
    total_price = models.DecimalField(decimal_places=3, max_digits=10, default=0)  #total price for all products in order
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=48)
    customer_address = models.CharField(max_length=128, default=' ')
    comments = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created =models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None,
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None,
                                on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(decimal_places=3, max_digits=10, default=0)
    total_price = models.DecimalField(decimal_places=3, max_digits=10, default=0) #price*nmb
    is_active = models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


