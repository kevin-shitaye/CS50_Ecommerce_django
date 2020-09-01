from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    items_name = models.CharField(max_length=30)
    watchers = models.ManyToManyField(User, related_name="watchlist_items", blank=True)
    current_price = models.FloatField()
    description = models.CharField(max_length=500)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    url_of_image = models.CharField(max_length=100)
    sold = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id}: {self.items_name}:- {self.current_price}"

class Bid(models.Model):
    asker = models.ForeignKey(User, blank=True, related_name="bidder", on_delete=models.CASCADE)
    item = models.ForeignKey(AuctionListing, blank=True, related_name="asked_prices", on_delete=models.CASCADE)
    ask_price = models.FloatField()


    def __str__(self):
        return f"{self.item} :- {self.ask_price} (BY {self.asker})"



class Comment(models.Model):
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="item_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.item} : {self.comment} (by {self.user})"


