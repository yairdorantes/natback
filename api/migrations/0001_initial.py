# Generated by Django 4.1.7 on 2023-03-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Pastel')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('price', models.FloatField(default=0, verbose_name='Precio')),
                ('weight', models.FloatField(default=0, verbose_name='Peso')),
                ('flavor', models.CharField(max_length=100, verbose_name='Sabor')),
            ],
        ),
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Dessert')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Insumo')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Material')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Producto')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
            ],
        ),
    ]