"""
This module contains the custom user model and other model related with create user model object
"""
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from common.models import BaseModel
from .custoomusermanager import CustomUserManager

class CustomUserModel(BaseModel,AbstractBaseUser,PermissionsMixin):
    """
    User model
    user can create account with a unique email 
    and each user have a unique identifier  generate with manager
    """
    email = models.EmailField(verbose_name='ایمیل',unique=True)
    user_identifier = models.CharField(verbose_name='شناساگر کاربر',unique=True)
    is_active = models.BooleanField(verbose_name='حساب کاربری فعال می باشد',default=False)
    is_admin = models.BooleanField(verbose_name='حساب کاربری دسترسی سطح ادمین دارد',default=False)

    USERNAME_FIELD = "email"

    objects= CustomUserManager()

    class Meta:
        """class Meta have a table info for User model"""
        ordering=['created_at',]
        verbose_name='حساب های کاربری'
        verbose_name_plural ='کاربران'

    def __str__(self)->str:
        """
        this method return a str about user email and identifier
        """
        return f"{self.email} ( {self.user_identifier} )"

    def is_staff(self)->bool:
        """
        this method return True if user admin else return False
        """
        return self.is_admin

    @property
    def is_verified(self)->bool:
        """
        Check email verified 
        """
        return self.is_active
