# Generated by Django 3.0.8 on 2020-08-30 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auctionlisting_sold'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
