# Generated by Django 4.2.3 on 2023-08-22 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todomodel_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='completed',
        ),
    ]
