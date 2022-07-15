from django.db import models

# Create your models here.
class BookingModel(models.Model):
    product_booking=models.CharField(max_length=50,null=True, blank=True)
    user_name=models.CharField(max_length=50,null=True, blank=True)
    password=models.CharField(max_length=50,null=True, blank=True)
    price=models.ImageField()

    def __str__(self):
        return self.product_booking

    class Meta:
        app_label = 'customer_data'

