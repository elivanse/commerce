# Generated by Django 4.1.dev20211210161305 on 2022-01-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('cs', 'Cabernet Sauvignon'), ('cf', 'Cabernet Franc'), ('pn', 'Pinot Noir'), ('sb', 'Sauvignon Blanc'), ('mt', 'Merlot'), ('pb', 'Pinot Blanc'), ('sh', 'Shiraz'), ('cd', 'Chardonnay'), ('sy', 'Syrah'), ('mc', 'Malbec')], max_length=67),
        ),
    ]
