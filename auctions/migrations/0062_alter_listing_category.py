# Generated by Django 4.1.dev20211210161305 on 2022-01-29 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0061_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('pb', 'Pinot Blanc'), ('pn', 'Pinot Noir'), ('sb', 'Sauvignon Blanc'), ('mt', 'Merlot'), ('cf', 'Cabernet Franc'), ('sh', 'Shiraz'), ('cd', 'Chardonnay'), ('mc', 'Malbec'), ('sy', 'Syrah'), ('cs', 'Cabernet Sauvignon')], max_length=67),
        ),
    ]
