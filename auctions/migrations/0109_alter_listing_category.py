# Generated by Django 4.1.dev20211210161305 on 2022-02-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0108_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('furniture', 'Furniture'), ('painting', 'Paintings'), ('phones', 'Phones'), ('wines', 'Wines'), ('clocks', 'Clocks')], max_length=67),
        ),
    ]
