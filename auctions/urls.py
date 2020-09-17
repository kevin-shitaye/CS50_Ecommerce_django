from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create"),
    path("listing/<int:item>", views.listingPage, name="listingPage"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("category/<str:category>", views.category, name="category")
]
