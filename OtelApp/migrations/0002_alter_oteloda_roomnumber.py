# Generated by Django 4.2.3 on 2023-10-09 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OtelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oteloda',
            name='roomnumber',
            field=models.IntegerField(default=1, verbose_name='Oda Numarası'),
        ),
    ]