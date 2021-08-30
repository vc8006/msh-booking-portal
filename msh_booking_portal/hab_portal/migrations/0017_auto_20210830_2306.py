# Generated by Django 3.2.5 on 2021-08-30 17:36

from django.db import migrations, models
import hab_portal.models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0016_alter_habmodel_fee_to_be_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habmodel',
            name='date_of_arrival',
            field=models.DateField(default=hab_portal.models.get_current_date, verbose_name='Date of Arrival'),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='department',
            field=models.CharField(max_length=256, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='email',
            field=models.CharField(max_length=500, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='hostel',
            field=models.CharField(choices=[('Lohit', 'Lohit'), ('Brahmaputra', 'Brahmaputra'), ('Umiam', 'Umiam'), ('Dihing', 'Dihing'), ('Disang', 'Disang'), ('Barak', 'Barak'), ('Kapili', 'Kapili'), ('Kameng', 'Kameng'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Dibang', 'Dibang'), ('Dhansiri', 'Dhansiri'), ('Subansiri', 'Subansiri')], max_length=256, verbose_name='Hostel'),
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
    ]