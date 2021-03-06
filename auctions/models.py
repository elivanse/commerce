from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import URLField

# Models: Your application should have at least three models in
# addition to the User model: one for auction listings,
# one for bids, and one for comments made on auction listings.
# It’s up to you to decide what fields each model should have,
# and what the types of those fields should be.
# You may have additional models if you would like.

dicCategorie = {
    ("furniture", "Furniture"),
    ("painting", "Paintings"),
    ("wines","Wines"),
    ("clocks","Clocks"),
    ("phones","Phones")
}

# usuarios


class User(AbstractUser):
    pass


class comment(models.Model):

    #idUser = models.ForeignKey(
    #    User, on_delete=models.CASCADE, related_name="comment_user")
    title = models.CharField(max_length=25, default="")
    comment = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, blank=True)

# ofertas


class bid(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.user} put the last bid in for {self.price}"

# subastas
class listing(models.Model):

    item = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=67, choices=dicCategorie)
    tophorizon = models.DateTimeField(auto_now_add=True, blank=True)
    # idUser = models.ForeignKey(
    #  User, on_delete=models.CASCADE, related_name="listing_user")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owners")
    bid = models.ManyToManyField(bid, blank=True, related_name="bid")
    comments = models.ManyToManyField(
        comment, blank=True, related_name="comments")
    photo = models.ImageField(null=True, blank=True)
    closed = models.BooleanField(default=False)

# favoritos


class watchlist(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="watchlist")
    listing = models.ForeignKey(
        listing,  on_delete=models.CASCADE, related_name="listing")
