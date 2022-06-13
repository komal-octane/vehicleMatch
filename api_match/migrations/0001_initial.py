# Generated by Django 4.0.5 on 2022-06-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=500, verbose_name='Model')),
                ('make', models.CharField(max_length=500, verbose_name='Make')),
                ('trim', models.CharField(max_length=250, verbose_name='Model_trim')),
            ],
        ),
    ]
