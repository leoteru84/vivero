# Generated by Django 4.1.4 on 2023-01-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_plantin_tamaño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='tamaño',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='frutal',
            name='tamaño',
            field=models.CharField(max_length=200),
        ),
    ]
