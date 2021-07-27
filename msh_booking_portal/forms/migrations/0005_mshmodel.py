# Generated by Django 3.2.5 on 2021-07-18 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_siteuser_data'),
        ('forms', '0004_samplemodel_locked'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSHModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_submission', models.DateTimeField(auto_now_add=True)),
                ('roll_number', models.IntegerField(verbose_name='Roll No.')),
                ('programme', models.CharField(max_length=256, verbose_name='Programme')),
                ('department', models.CharField(max_length=256, verbose_name='Department')),
                ('address_present', models.TextField(verbose_name='Present Address')),
                ('pincode_present', models.IntegerField(verbose_name='Pincode')),
                ('phone_number_present', models.IntegerField(verbose_name='Phone Number')),
                ('address_permanent', models.TextField(verbose_name='Permanent Address')),
                ('pincode_permanent', models.IntegerField(verbose_name='Pincode')),
                ('phone_number_permanent', models.IntegerField(verbose_name='Phone Number')),
                ('date_of_marriage', models.DateField(verbose_name='Date of Marriage')),
                ('name_of_spouse', models.CharField(max_length=256, verbose_name='Name of Spouse')),
                ('age_of_spouse', models.IntegerField(verbose_name='Age of Spouse')),
                ('occupation_of_spouse', models.CharField(blank=True, max_length=256, verbose_name='Occupation of Spouse')),
                ('place_of_employment_of_spouse', models.TextField(blank=True, verbose_name='Place of Employment of Spouse')),
                ('dependents', models.TextField(blank=True, verbose_name='Dependents')),
                ('date_by_which_you_intend_to_bring_family', models.DateField(verbose_name='Date by which you intend to bring your Family')),
                ('locked', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.siteuser')),
            ],
        ),
    ]