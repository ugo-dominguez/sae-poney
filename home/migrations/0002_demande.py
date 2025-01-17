# Generated by Django 5.1.4 on 2025-01-17 17:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('idDemande', models.AutoField(primary_key=True, serialize=False)),
                ('dateCou', models.DateTimeField()),
                ('duree', models.PositiveSmallIntegerField()),
                ('accepte', models.BooleanField()),
                ('demandeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('duree__gte', 1), ('duree__lte', 2)), name='demande_check_duree_range')],
            },
        ),
    ]
