# Generated by Django 3.2.2 on 2021-11-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
