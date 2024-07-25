from django.shortcuts import redirect, render

from administration.models import Caroussel, Actualite, Produit

from django.views.generic import ListView, DetailView

from django.core.mail import send_mail, BadHeaderError

from django.conf import settings

from django.contrib import messages


produits = Produit.objects.all()

products_keys = []

for prod in produits:
    products_keys.append(int(prod.pk))

products_keys = sorted(products_keys)

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

        return render(request, f"saar_website/produits/produit-{numero}.html", context=context)
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


def about_grp(request):

    context = {}

    context['products_keys'] = products_keys

    return render(request, "saar_website/about_grp.html", context=context)


def contact(request):

    context = {}

    context['active_contact'] = 'active_contact'

    context['products_keys'] = products_keys

    if request.method == 'POST':
        name = request.POST['name']
        from_email = request.POST['from_email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject=f'{subject}', message=f'{message} {name} {from_email}', from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.EMAIL_HOST_USER])

        message = f"Votre message a bien été envoyé, un de nos conseiller vous contacteras dans un bref délai."
        messages.success(request, message)

        return redirect('contact')


    return render(request, "saar_website/contact.html", context=context)


def agences(request):

    context = {}

    context['active_agences'] = 'active_agences'

    context['products_keys'] = products_keys

    return render(request, "saar_website/agences.html", context=context)



def reclamation(request):

    context = {}

    # context['active_agences'] = 'active_agences'

    context['products_keys'] = products_keys

    return render(request, "saar_website/reclamation.html", context=context)



def valeurs(request):

    context = {}

    # context['active_agences'] = 'active_agences'

    context['products_keys'] = products_keys

    return render(request, "saar_website/valeurs.html", context=context)



