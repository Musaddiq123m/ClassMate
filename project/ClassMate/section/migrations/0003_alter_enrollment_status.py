# Generated by Django 5.1 on 2024-11-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('Enrolled', 'Enrolled'), ('Dropped', 'Dropped'), ('Completed', 'Completed')], default='Enrolled', max_length=20),
        ),
    ]
