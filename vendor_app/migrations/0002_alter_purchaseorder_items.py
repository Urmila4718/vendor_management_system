# Generated by Django 4.2.11 on 2024-04-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.TextField(),
        ),
    ]
