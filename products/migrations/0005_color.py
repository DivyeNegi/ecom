# Generated by Django 5.1.2 on 2024-10-29 07:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_storage_price_increase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('color_title', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_variants', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]