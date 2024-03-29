# Generated by Django 2.2 on 2019-06-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adult_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('sales_price', models.IntegerField()),
                ('original_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Essential_Oils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('sales_price', models.IntegerField()),
                ('original_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Smart_Watches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('sales_price', models.IntegerField()),
                ('original_price', models.IntegerField()),
            ],
        ),
    ]
