# Generated by Django 5.1.5 on 2025-06-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_cartitem_size_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='size',
            field=models.CharField(default='M', max_length=2),
        ),
    ]
