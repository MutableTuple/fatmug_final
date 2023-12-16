# Generated by Django 4.2.8 on 2023-12-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_alter_purchaseorder_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendormodel',
            name='fulfillment_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_code',
            field=models.CharField(blank=True, default='C3ZCU', max_length=15, null=True),
        ),
    ]