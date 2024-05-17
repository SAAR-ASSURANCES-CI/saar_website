from django.shortcuts import render

from administration.models import Caroussel, Actualite, Produit

from django.views.generic import ListView, DetailView


produits = Produit.objects.all()

products_keys = []

for prod in produits:
    products_keys.append(prod.pk)

def index(request):

    context = {}

    # Carousel

    carousels = Caroussel.objects.all()
    actualites = Actualite.objects.all()
    produits = Produit.objects.all()

    

    context['carousels'] = carousels
    context['actualites'] = actualites
    context['produits'] = produits

    context['products_keys'] = products_keys

    context['active_index'] = 'active_index'

    return render(request, "saar_website/index.html", context=context)


def carousel(request, numero):

    try:
        context = {}
        carousel = Caroussel.objects.get(pk=numero)

        context['carousel'] = carousel
        context['products_keys'] = products_keys
        context['active_carousel'] = 'active_carousel'

        return render(request, f"saar_website/carousel/carousels.html", context=context)
    except:
        return render(request, "saar_website/404.html", context=context)
    

def produit(request, numero):

    try:
        context = {}
        produit = Produit.objects.get(pk=numero)

        context['produit'] = produit
        context['products_keys'] = products_keys
        context[f'active_produit{numero}'] = f'active_produit{numero}'

        return render(request, f"saar_website/produit/produits.html", context=context)
    except:
        return render(request, "saar_website/404.html", context=context)    
    

# class CarouselListView(ListView):
#     model = Caroussel
#     template_name = "saar_website/index.html"


# class CarouselDetailView(DetailView):
#     model = Caroussel
#     template_name = "saar_website/carousel/carousels.html"


def about(request):

    context = {}

    context['active_about'] = 'active_about'

    context['products_keys'] = products_keys

    return render(request, "saar_website/about.html", context=context)


def contact(request):

    context = {}

    context['active_contact'] = 'active_contact'

    context['products_keys'] = products_keys

    return render(request, "saar_website/contact.html", context=context)


def agences(request):

    context = {}

    context['active_agences'] = 'active_agences'

    context['products_keys'] = products_keys

    return render(request, "saar_website/agences.html", context=context)



