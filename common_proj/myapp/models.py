from django.db import models

# Create your models here.


from .managers import UserManager

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
# from django.db.models.signals import post_save, pre_save
# Create your models here.

USER_ROLES = (
    ('Admin','Admin'),
    ('SubAdmin','SubAdmin'),
    ('User','User'),
    ('Trainer','Trainer'),
    ('Gym Owner','Gym Owner'),
    ('Customer','Customer')
)
GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
)
class User(AbstractBaseUser):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255,null=True,blank=True)
    user_role = models.CharField(max_length=40,choices=USER_ROLES,null=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(unique = True)         
    password = models.CharField(max_length=255,null=True,blank=True)               
    
   

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    def __str__(self):
        """Return full name in representation instead of objects"""
        return self.email
    
    class Meta:
        """A meta object for defining name of the user table"""
        db_table = "user" 
        
        

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()