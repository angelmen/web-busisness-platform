# Generated by Django 2.0.7 on 2019-04-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20190419_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='existencias',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='articulo_venta',
            name='existencias',
            field=models.SmallIntegerField(),
        ),
    ]