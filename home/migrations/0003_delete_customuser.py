# Generated by Django 5.1.4 on 2025-01-17 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
