# Generated by Django 3.2.5 on 2021-07-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0022_alter_habmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habmodel',
            name='status',
            field=models.CharField(choices=[('0', 'Approved'), ('1', 'Pending'), ('-1', 'Rejected')], default='1', max_length=256),
        ),
    ]
