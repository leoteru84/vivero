# Generated by Django 4.1.4 on 2023-01-29 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_remove_entrada_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=models.TextField(),
        ),
    ]