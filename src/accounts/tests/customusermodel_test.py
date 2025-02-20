from django.test import TestCase
from django.core.exceptions import ValidationError

from src.accounts.models import CustomUserModel

class UserModelTest(TestCase):
    """
    this class try to test CustomUserModel    
    """
    def __init__(self):
        self.data  = {'email':'example@gmil.com'}
    
    def test_usermodel_create_user(self):
        
        user = CustomUserModel.objects.create_user(**self.data)
        self.assertIsInstance(user,CustomUserModel)
