# Generated by Django 5.1 on 2024-11-22 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
    ]
