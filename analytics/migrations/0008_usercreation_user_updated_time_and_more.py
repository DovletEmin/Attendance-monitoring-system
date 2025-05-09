# Generated by Django 5.1.7 on 2025-04-06 05:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_delete_attendancerecord_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreation',
            name='user_updated_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usercreation',
            name='user_updated_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
