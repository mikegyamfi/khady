# Generated by Django 4.2.4 on 2024-07-19 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0028_alter_shipmentstatus_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, unique=True)),
                ('loaded_date', models.DateTimeField()),
                ('received_date', models.DateTimeField()),
                ('estimated_date_of_arrival', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=20, unique=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='intel_app.shippingorder')),
            ],
        ),
        migrations.RemoveField(
            model_name='shippingtrackinginfo',
            name='shipment_status',
        ),
        migrations.DeleteModel(
            name='ShipmentStatus',
        ),
        migrations.DeleteModel(
            name='ShippingTrackingInfo',
        ),
        migrations.DeleteModel(
            name='StatusName',
        ),
        migrations.AddField(
            model_name='package',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='intel_app.shippingorder'),
        ),
    ]
