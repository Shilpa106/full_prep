from django.db import models

# Create your models here.
class GeeksModel(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title