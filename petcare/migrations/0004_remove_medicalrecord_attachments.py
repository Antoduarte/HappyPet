# Generated by Django 4.2.20 on 2025-05-16 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petcare', '0003_medicalattachment_medicalrecord_attachments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='attachments',
        ),
    ]
