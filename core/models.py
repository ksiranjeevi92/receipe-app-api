from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        '''create and save user'''
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save()

        return user
class User(AbstractBaseUser,PermissionsMixin):
    '''customer user model that use email instead of username'''
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
