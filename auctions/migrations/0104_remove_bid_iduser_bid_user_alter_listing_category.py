# Generated by Django 4.1.dev20211210161305 on 2022-02-11 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0103_bid_iduser_alter_listing_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='idUser',
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_bids', to='auctions.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('painting', 'Paintings'), ('phones', 'Phones'), ('clocks', 'Clocks'), ('furniture', 'Furniture'), ('wines', 'Wines')], max_length=67),
        ),
    ]
