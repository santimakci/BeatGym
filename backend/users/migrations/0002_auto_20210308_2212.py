# Generated by Django 2.2.19 on 2021-03-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_recruiter',
            new_name='pay_last_month',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_started',
            field=models.DateTimeField(null=True),
        ),
    ]