from django.db import models

# Create your models here.
class HomePageOffersCarousel(models.Model):
    itemName = models.CharField(max_length=100)
    itemDescription= models.TextField()
    itemOffer = models.CharField(max_length=100)
    itemImage = models.ImageField(upload_to='pics') 
