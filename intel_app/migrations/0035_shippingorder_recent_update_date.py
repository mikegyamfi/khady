# Generated by Django 4.2.4 on 2024-07-21 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0034_alter_shippingorder_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingorder',
            name='recent_update_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]