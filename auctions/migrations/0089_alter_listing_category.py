# Generated by Django 4.0.2 on 2022-02-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0088_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('phones', 'Phones'), ('painting', 'Paintings'), ('clocks', 'Clocks'), ('furniture', 'Furniture'), ('wines', 'Wines')], max_length=67),
        ),
    ]
