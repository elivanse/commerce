# Generated by Django 4.0.2 on 2022-02-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0091_alter_listing_category_alter_listing_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('furniture', 'Furniture'), ('clocks', 'Clocks'), ('wines', 'Wines'), ('painting', 'Paintings'), ('phones', 'Phones')], max_length=67),
        ),
    ]
