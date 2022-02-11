# Generated by Django 4.1.dev20211210161305 on 2022-02-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0082_alter_listing_category_alter_listing_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('pb', 'Pinot Blanc'), ('pn', 'Pinot Noir'), ('sy', 'Syrah'), ('sb', 'Sauvignon Blanc'), ('sh', 'Shiraz'), ('cd', 'Chardonnay'), ('cf', 'Cabernet Franc'), ('mt', 'Merlot'), ('cs', 'Cabernet Sauvignon'), ('mc', 'Malbec')], max_length=67),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]