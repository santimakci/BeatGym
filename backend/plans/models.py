from django.db import models
from users.models import User
from ckeditor.fields import RichTextField

class Plan(models.Model):
    
    phase = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plan')
    date_start = models.DateTimeField(null=False)
    date_end = models.DateTimeField(null=False)
    objetives = RichTextField(null=True)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} '
