# Generated by Django 5.1 on 2024-12-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='starred',
            field=models.BooleanField(default=False),
        ),
    ]
