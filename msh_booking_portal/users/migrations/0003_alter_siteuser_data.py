# Generated by Django 3.2.5 on 2021-07-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_siteuser_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='data',
            field=models.TextField(blank=True),
        ),
    ]