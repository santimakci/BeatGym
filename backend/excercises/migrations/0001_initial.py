# Generated by Django 2.2.19 on 2021-03-08 23:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcerciseName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=15, null=True)),
                ('repetitions', models.CharField(max_length=15, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('excercise_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='excercise_name', to='excercises.ExcerciseName')),
                ('plan_excercises', models.ManyToManyField(to='plans.Plan')),
            ],
        ),
    ]
