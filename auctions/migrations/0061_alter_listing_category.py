# Generated by Django 4.1.dev20211210161305 on 2022-01-29 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0060_rename_wltitle_watchlist_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('pn', 'Pinot Noir'), ('sb', 'Sauvignon Blanc'), ('mc', 'Malbec'), ('mt', 'Merlot'), ('cs', 'Cabernet Sauvignon'), ('cd', 'Chardonnay'), ('pb', 'Pinot Blanc'), ('cf', 'Cabernet Franc'), ('sh', 'Shiraz'), ('sy', 'Syrah')], max_length=67),
        ),
    ]
