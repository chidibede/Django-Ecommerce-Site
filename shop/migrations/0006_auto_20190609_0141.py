# Generated by Django 2.2 on 2019-06-09 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190609_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adult_product',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='essential_oil',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='smart_watch',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
