# Generated by Django 5.1.2 on 2024-10-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_storage_variant_storage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='price_increase',
            field=models.IntegerField(),
        ),
    ]