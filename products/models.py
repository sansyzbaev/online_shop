from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None,
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_active = models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.id
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'