# Generated by Django 4.2.1 on 2023-07-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0004_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenUrl',
            field=models.ImageField(null=True, upload_to='imgProducto'),
        ),
    ]