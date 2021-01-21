from django.shortcuts import render
from .models import HomePageOffersCarousel

# Create your views here.
def home(request):
    items = HomePageOffersCarousel.objects.all()
    return render(request,"index.html", {'items':items})