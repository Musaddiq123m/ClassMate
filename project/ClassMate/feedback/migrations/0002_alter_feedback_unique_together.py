# Generated by Django 5.1 on 2024-12-01 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
        ('section', '0004_section_finalized'),
        ('user', '0003_remove_customuser_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together={('student', 'section', 'feedback_text')},
        ),
    ]
