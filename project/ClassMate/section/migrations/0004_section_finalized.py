# Generated by Django 5.1 on 2024-11-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0003_alter_enrollment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='finalized',
            field=models.BooleanField(default=False),
        ),
    ]
