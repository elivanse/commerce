# Generated by Django 4.1.dev20211210161305 on 2022-01-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0064_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('sb', 'Sauvignon Blanc'), ('pb', 'Pinot Blanc'), ('sh', 'Shiraz'), ('mc', 'Malbec'), ('mt', 'Merlot'), ('sy', 'Syrah'), ('cd', 'Chardonnay'), ('cf', 'Cabernet Franc'), ('cs', 'Cabernet Sauvignon'), ('pn', 'Pinot Noir')], max_length=67),
        ),
    ]
