# Generated by Django 4.2.4 on 2024-07-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0036_customuser_unique_shipping_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='cbm',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='estimated_date_of_arrival',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='loaded_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='received_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
