from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import AuctionListing,User,Bid,Comment



def index(request):
    return render(request, "auctions/index.html", {
        "items":AuctionListing.objects.all().exclude(sold__exact = True)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    if request.method == "POST":
        items_name = request.POST['items_name']
        price = request.POST['price']
        url_for_image = request.POST['image']
        category = request.POST['category']
        description = request.POST['description']
        item = AuctionListing(items_name=items_name, current_price=price, description=description, category=category, url_of_image=url_for_image, provider=request.user)
        item.save()
        return render(request, "auctions/create_listing.html")
    else:
        return render(request, "auctions/create_listing.html")


def listingPage(request, item):
    user = request.user
    item = AuctionListing.objects.get(id=item)
    if request.method == "POST":
        if 'watchlist' in request.POST:
            if request.POST['watchlist'] == "Add to watchlist":
                item.watchers.add(user)
            else:
                item.watchers.remove(user)
            return render(request, 'auctions/listingPage.html', {
                "item": item,
                "user":user,
                "bids": Bid.objects.filter(item__exact=item).order_by("-ask_price")[1:6],
                "comments": Comment.objects.filter(item__exact=item)
            })
        elif 'bid' in request.POST:
            ask_price = request.POST['ask']
            bid = Bid(ask_price=ask_price, asker=user, item=item)
            bid.save()
            item.current_price = int(ask_price)
            item.save()
            return HttpResponseRedirect(reverse("index"))
        elif 'sold' in request.POST:
            item.sold = True
            item.save()
            return HttpResponseRedirect(reverse("index"))
        elif 'comment' in request.POST:
            comment = request.POST['comments']
            # creating the comment
            com = Comment(item=item, user=user, comment=comment)
            com.save()
            return render(request, 'auctions/listingPage.html', {
                "item": item,
                "user": user,
                "bids": Bid.objects.filter(item__exact=item).order_by("-ask_price")[1:6],
                "comments": Comment.objects.filter(item__exact=item)
            })
    else:
        return render(request, 'auctions/listingPage.html', {
            "item":item,
            "user":user,
            "bids":Bid.objects.filter(item__exact=item).order_by("-ask_price")[:6],
            "comments":Comment.objects.filter(item__exact=item)
        })


@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "items":AuctionListing.objects.filter(watchers__exact=request.user)
    })


def category(request):
    if request.method == 'POST':
        cate = request.POST['category']
        return render(request, "auctions/categoryPage.html", {
            "items": AuctionListing.objects.filter(category__exact=cate)
        })
    return render(request, "auctions/category.html", {
        "items":AuctionListing.objects.all()
    })
