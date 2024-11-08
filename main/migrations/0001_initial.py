# Generated by Django 5.0.7 on 2024-11-04 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Water', 'Water'), ('Food', 'Food')], max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('level', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=6)),
                ('status', models.CharField(choices=[('Well', 'Well'), ('Normal', 'Normal'), ('Bad', 'Bad')], max_length=7)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factors', to='main.location')),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('total_count', models.IntegerField()),
                ('male_count', models.IntegerField()),
                ('female_count', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='populations', to='main.location')),
            ],
        ),
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threats', to='main.location')),
            ],
        ),
    ]
