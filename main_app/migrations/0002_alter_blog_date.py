# Generated by Django 3.2.4 on 2021-08-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(verbose_name='trip date'),
        ),
    ]
