from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserObjectManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None):
        if not email:
            raise ValueError("User have to have an email address ")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone_number=phone_number)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, phone_number,  password):
        user = self.create_user(username, email, phone_number, password)
        user.is_superuser = True
        user.is_staff = True

        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255, 
        unique=True, 
        verbose_name="Email Address"
    )
    username = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserObjectManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number"]

    def __str__(self):
        return self.email
