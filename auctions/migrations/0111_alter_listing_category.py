# Generated by Django 4.1.dev20211210161305 on 2022-02-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0110_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('phones', 'Phones'), ('clocks', 'Clocks'), ('wines', 'Wines'), ('painting', 'Paintings'), ('furniture', 'Furniture')], max_length=67),
        ),
    ]
