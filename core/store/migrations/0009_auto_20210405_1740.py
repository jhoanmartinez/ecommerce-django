# Generated by Django 3.1.7 on 2021-04-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]