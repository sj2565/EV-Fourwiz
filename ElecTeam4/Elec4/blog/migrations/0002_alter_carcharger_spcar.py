# Generated by Django 3.2.7 on 2021-10-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carcharger',
            name='spCar',
            field=models.CharField(max_length=100),
        ),
    ]
