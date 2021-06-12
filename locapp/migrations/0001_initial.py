# Generated by Django 3.1.2 on 2021-04-28 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=150)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationCityDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_name', models.CharField(max_length=50)),
                ('destinationImage', models.ImageField(blank=True, null=True, upload_to='destinationImages')),
                ('destination_desc', models.CharField(max_length=256)),
                ('destination_extras', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tourist_name', models.CharField(max_length=30)),
                ('tourist_latitude', models.FloatField(null=True)),
                ('tourist_longitude', models.FloatField(null=True)),
                ('tourist_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationMetaDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_destination_name', models.CharField(max_length=60)),
                ('meta_destination_Image', models.ImageField(upload_to='metadestinationImages')),
                ('meta_destination_desc', models.CharField(max_length=256)),
                ('destination_extras', models.CharField(max_length=200)),
                ('admin_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('meta_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locapp.destinationcitydetails')),
            ],
        ),
    ]
