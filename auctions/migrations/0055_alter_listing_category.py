# Generated by Django 4.1.dev20211210161305 on 2022-01-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0054_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sy', 'Syrah'), ('pn', 'Pinot Noir'), ('cf', 'Cabernet Franc'), ('mt', 'Merlot'), ('sb', 'Sauvignon Blanc'), ('cd', 'Chardonnay'), ('pb', 'Pinot Blanc'), ('mc', 'Malbec'), ('cs', 'Cabernet Sauvignon'), ('sh', 'Shiraz')], max_length=67),
        ),
    ]