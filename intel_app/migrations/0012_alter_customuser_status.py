# Generated by Django 5.0 on 2024-01-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0011_afaregistration2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('User', 'User'), ('Agent', 'Agent'), ('Super Agent', 'Super Agent')], default='User', max_length=250),
        ),
    ]
