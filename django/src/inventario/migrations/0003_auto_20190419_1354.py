# Generated by Django 2.0.7 on 2019-04-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20190419_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='codigoProducto',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='nombreProducto',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='ubicacion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='articulo_venta',
            name='codigoProducto',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='articulo_venta',
            name='nombreProducto',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='articulo_venta',
            name='ubicacion',
            field=models.CharField(max_length=50),
        ),
    ]