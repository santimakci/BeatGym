# Generated by Django 2.2.19 on 2021-05-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210525_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
