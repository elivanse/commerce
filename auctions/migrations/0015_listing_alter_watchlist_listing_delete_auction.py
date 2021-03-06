# Generated by Django 4.1.dev20211210161305 on 2021-12-12 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_auction_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('sb', 'Sauvignon Blanc'), ('mc', 'Malbec'), ('mt', 'Merlot'), ('cd', 'Chardonnay'), ('pn', 'Pinot Noir'), ('pb', 'Pinot Blanc'), ('sy', 'Syrah'), ('cs', 'Cabernet Sauvignon'), ('sh', 'Shiraz'), ('cf', 'Cabernet Franc')], max_length=67)),
                ('tophorizon', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('closed', models.BooleanField(default=False)),
                ('bids', models.ManyToManyField(blank=True, related_name='bids', to='auctions.bids')),
                ('comments', models.ManyToManyField(blank=True, related_name='comments', to='auctions.comment')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_user', to='auctions.user')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='auctions.user')),
            ],
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='auctions.listing'),
        ),
        migrations.DeleteModel(
            name='auction',
        ),
    ]
