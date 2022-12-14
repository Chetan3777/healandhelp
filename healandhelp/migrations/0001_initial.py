# Generated by Django 4.0.3 on 2022-09-22 14:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('all_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=10000, null=True)),
                ('ref_no', models.CharField(blank=True, max_length=10000, null=True)),
                ('address', models.CharField(blank=True, max_length=10000, null=True)),
                ('locality', models.CharField(blank=True, max_length=10000, null=True)),
                ('city', models.CharField(blank=True, max_length=10000, null=True)),
                ('state', models.CharField(blank=True, max_length=10000, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=10000, null=True)),
                ('country', models.CharField(blank=True, max_length=10000, null=True)),
                ('mobileno', models.CharField(blank=True, max_length=10000, null=True, unique=True)),
                ('refrenced_by', models.CharField(blank=True, max_length=10000, null=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('maritialstatus', models.CharField(blank=True, max_length=100, null=True)),
                ('medication', models.CharField(blank=True, max_length=100, null=True)),
                ('allergies', models.CharField(blank=True, max_length=100, null=True)),
                ('height', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_name', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_contact_no', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_relationship', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_details.branch', verbose_name='Branch')),
            ],
            options={
                'verbose_name': 'Website',
            },
        ),
    ]
