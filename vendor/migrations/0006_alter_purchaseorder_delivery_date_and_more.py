# Generated by Django 4.2.8 on 2023-12-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_vendormodel_total_po_cancelled_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_code',
            field=models.CharField(blank=True, default='7MQ99', max_length=15, null=True),
        ),
    ]