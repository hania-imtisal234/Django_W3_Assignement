# Generated by Django 5.1 on 2024-09-10 09:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_alter_appointment_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='appointment',
            index=models.Index(fields=['doctor'], name='appointment_doctor__649ad1_idx'),
        ),
        migrations.AddIndex(
            model_name='appointment',
            index=models.Index(fields=['patient'], name='appointment_patient_94a7ef_idx'),
        ),
        migrations.AddIndex(
            model_name='appointment',
            index=models.Index(fields=['scheduled_at'], name='appointment_schedul_7069dc_idx'),
        ),
    ]
