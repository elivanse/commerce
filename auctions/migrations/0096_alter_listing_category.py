# Generated by Django 4.0.2 on 2022-02-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0095_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('furniture', 'Furniture'), ('wines', 'Wines'), ('clocks', 'Clocks'), ('phones', 'Phones'), ('painting', 'Paintings')], max_length=67),
        ),
    ]