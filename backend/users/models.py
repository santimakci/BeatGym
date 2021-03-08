from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    modified = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, upload_to='users')
    observations = RichTextField(null=True)
    phone = models.CharField(null=True, max_length=15)
    date_of_birth = models.DateTimeField(null=True)
    date_of_started =models.DateTimeField(null=True)
    pay_last_month = models.BooleanField(default=False)
