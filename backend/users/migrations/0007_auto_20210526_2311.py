# Generated by Django 2.2.19 on 2021-05-26 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210526_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_started',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]