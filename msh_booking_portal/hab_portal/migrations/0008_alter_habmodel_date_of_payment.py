# Generated by Django 3.2.5 on 2021-08-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0007_alter_habmodel_date_of_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habmodel',
            name='date_of_payment',
            field=models.DateField(verbose_name='Date of Payment'),
        ),
    ]