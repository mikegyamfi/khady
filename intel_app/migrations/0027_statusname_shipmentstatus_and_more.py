# Generated by Django 4.2.4 on 2024-05-25 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0026_product_preorder_arrival_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='intel_app.shippingtrackinginfo')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intel_app.statusname')),
            ],
        ),
        migrations.AlterField(
            model_name='shippingtrackinginfo',
            name='shipment_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='intel_app.statusname'),
        ),
    ]
