# Generated by Django 3.0.8 on 2020-08-27 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_delete_bids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask_price', models.FloatField()),
                ('asker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='asked_prices', to='auctions.AuctionListing')),
            ],
        ),
    ]
