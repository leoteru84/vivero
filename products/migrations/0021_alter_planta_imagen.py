# Generated by Django 4.1.4 on 2023-01-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_planta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/PLANTA/'),
        ),
    ]