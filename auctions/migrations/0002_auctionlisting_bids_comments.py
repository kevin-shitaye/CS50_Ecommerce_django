# Generated by Django 3.0.8 on 2020-08-25 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_name', models.CharField(max_length=30)),
                ('current_price', models.FloatField()),
                ('description', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=30)),
                ('url_of_image', models.CharField(max_length=100)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('item', models.ManyToManyField(blank=True, related_name='item_comments', to='auctions.AuctionListing')),
                ('user', models.ManyToManyField(blank=True, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask_price', models.FloatField()),
                ('asker', models.ManyToManyField(blank=True, related_name='bidder', to=settings.AUTH_USER_MODEL)),
                ('item', models.ManyToManyField(blank=True, related_name='asked_prices', to='auctions.AuctionListing')),
            ],
        ),
    ]
