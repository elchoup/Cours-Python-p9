from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {"bands": bands}
                  )


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def about(request):
    return render(request, "listings/about.html")


def listings(request):
    listings = Listing.objects.all()
    return render(request, 
                  "listings/listings.html",
                  {"listings": listings})
    

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listing})


def contact(request):
    if request.method == "POST":
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
                  "listings/contact.html",
                  {'form': form})
