from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    modified = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, null=True, upload_to='users')
    observations = RichTextField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_started = models.DateField(blank=True, null=True)
    pay_last_month = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

