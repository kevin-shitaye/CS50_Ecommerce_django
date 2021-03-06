# Generated by Django 3.0.8 on 2020-08-27 19:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctionlisting_watchlist_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='watchlist_item',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='watchers',
            field=models.ManyToManyField(blank=True, related_name='watchlist_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
