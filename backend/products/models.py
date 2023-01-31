from django.db import models

# Create your models here.

class Product(models.Model):
    title =models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

# adding custom fields in model through serializers
    @property
    def sale_price(self):
        try:
            return "%.2f" %(float(self.price)*0.8)
        except:
            return None

    def get_discount(self):
        try:
            return (self.price + 100)
        except:
            return None
