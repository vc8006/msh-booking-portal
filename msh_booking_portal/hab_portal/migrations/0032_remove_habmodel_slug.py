# Generated by Django 3.2.5 on 2021-08-04 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0031_alter_habmodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habmodel',
            name='slug',
        ),
    ]
