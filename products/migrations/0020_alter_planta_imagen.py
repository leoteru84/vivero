# Generated by Django 4.1.4 on 2023-01-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_planta_options_alter_planta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='PLANTA'),
        ),
    ]
