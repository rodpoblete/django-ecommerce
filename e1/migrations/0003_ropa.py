# Generated by Django 4.1 on 2022-11-28 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e1', '0002_electro'),
    ]

    operations = [
        migrations.CreateModel(
            name='ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Producto', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=10)),
                ('stock', models.CharField(max_length=4)),
            ],
        ),
    ]
