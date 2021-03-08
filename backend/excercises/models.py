from django.db import models
from plans.models import Plan
from ckeditor.fields import RichTextField

class ExcerciseName(models.Model):
    name = RichTextField(null=False)

    def __str__(self):
        return f'{self.name} '

class Excercise(models.Model):
    
    plan_excercises = models.ManyToManyField(Plan)
    excercise_name = models.ForeignKey(ExcerciseName, on_delete=models.DO_NOTHING ,related_name='excercise_name')
    series = models.CharField(null=True, max_length=15)
    repetitions = models.CharField(null=True, max_length=15)
    weight = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.excercise_name.name} '



