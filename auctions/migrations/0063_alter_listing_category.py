# Generated by Django 4.1.dev20211210161305 on 2022-01-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0062_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('pn', 'Pinot Noir'), ('sy', 'Syrah'), ('cs', 'Cabernet Sauvignon'), ('mc', 'Malbec'), ('cf', 'Cabernet Franc'), ('cd', 'Chardonnay'), ('mt', 'Merlot'), ('pb', 'Pinot Blanc'), ('sb', 'Sauvignon Blanc'), ('sh', 'Shiraz')], max_length=67),
        ),
    ]