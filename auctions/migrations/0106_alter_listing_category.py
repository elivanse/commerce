# Generated by Django 4.1.dev20211210161305 on 2022-02-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0105_remove_bid_user_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('painting', 'Paintings'), ('clocks', 'Clocks'), ('furniture', 'Furniture'), ('phones', 'Phones'), ('wines', 'Wines')], max_length=67),
        ),
    ]
