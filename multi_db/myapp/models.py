from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=899)
    address=models.CharField(max_length=899)
    phone=models.CharField(max_length=899)
    gender=models.CharField(max_length=8)
    color=models.CharField(max_length=899)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'user_data'
    