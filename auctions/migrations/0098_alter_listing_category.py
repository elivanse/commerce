# Generated by Django 4.0.2 on 2022-02-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0097_alter_listing_category_alter_listing_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('wines', 'Wines'), ('phones', 'Phones'), ('clocks', 'Clocks'), ('painting', 'Paintings'), ('furniture', 'Furniture')], max_length=67),
        ),
    ]
