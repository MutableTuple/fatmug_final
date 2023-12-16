# Generated by Django 4.2.8 on 2023-12-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_vendormodel_vendor_code_performancerecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.JSONField(default={'FR': 'Freshman', 'GR': 'Graduate', 'JR': 'Junior', 'SO': 'Sophomore', 'SR': 'Senior'}),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_code',
            field=models.CharField(blank=True, default='43LHA', max_length=15, null=True),
        ),
    ]