"""
This module contains the custom user manager for the accounts app.
"""
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User =get_user_model()
class CustomUserManager(BaseUserManager):
    """
    custom user manager 
    managed user model, generate unique identifier for each user and etc
    
    """
    def generate_unique_user_identifier(self):
        while True:
            random_id=get_random_string(length=32)
            if not User.objects.filter(user_identifier=random_id).exists():
                return random_id
    def create_user(self, email,is_active=False,is_admin=False,password = None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email.lower()),
                          is_active=is_active,is_admin=is_admin)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.user_identifier=self.generate_unique_user_identifier()
        user.full_clean()
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password):
        user = self.create_user(email=email,password=password,is_active=True,is_admin=True)
        return user
    