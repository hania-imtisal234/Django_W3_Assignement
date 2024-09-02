# Generated by Django 5.1 on 2024-09-02 14:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical_records', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_record_doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_record_patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
