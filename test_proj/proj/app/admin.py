from django.contrib import admin

# Register your models here.
from .models import GeeksModel,Product ,Item
admin.site.register(GeeksModel)
admin.site.register(Product)
admin.site.register(Item)
