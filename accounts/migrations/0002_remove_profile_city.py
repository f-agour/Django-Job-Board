# Generated by Django 4.2.6 on 2023-11-01 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
    ]
