from django.db import models

# Create your models here.
from django.db import models
# from django.model.postgres import ArrayField
from django.contrib.postgres.fields import ArrayField
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title

choices = [
    ('blue', 'blue'),
    ('red', 'red')
    ]


class Product(models.Model):
    name = models.CharField(max_length=100)
    # id = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=choices)
    question_array = ArrayField(models.IntegerField(null=True, blank=True), blank=True,)
    address=models.CharField(max_length=255,null=True, blank=True)
    address2=models.CharField(max_length=255,null=True, blank=True)
    

class Item(models.Model):
   
    board = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )

    # req = ArrayField(null=True)
    # response = ArrayField(null=True)
