# Generated by Django 4.2.5 on 2023-12-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0007_emailaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='purchase_count',
            field=models.IntegerField(default=0),
        ),
    ]
