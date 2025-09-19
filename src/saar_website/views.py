from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from administration.models import Agence, AgentGeneral, Caroussel, Actualite, DetailProduit, Formule, Garantie, Produit, Sinistre, Temoignage

from django.views.generic import ListView, DetailView

from django.core.mail import send_mail, BadHeaderError

from django.core.mail import EmailMessage

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from django.template.loader import render_to_string

from django.conf import settings

from django.contrib import messages

from administration.forms import SinistreForm

from weasyprint import HTML, CSS

import pandas as pd

from datetime import datetime

produits = Produit.objects.all()

produits_nonvie = Produit.objects.filter(categorie_id=1)
produits_vie = Produit.objects.filter(categorie_id=2)
produits_takaful = Produit.objects.filter(categorie_id=3).first()


products_keys = []

for prod in produits:
    products_keys.append(int(prod.pk))

products_keys = sorted(products_keys)

def index(request):

    context = {}

    # Carousel

    carousels = Caroussel.objects.all()
    actualites = Actualite.objects.order_by('-date_publication')
    produits = Produit.objects.all()
    temoignages = Temoignage.objects.all()

    produits_nonvie_visibles = Produit.objects.filter(categorie_id=1).filter(is_visible=True)
    produits_vie_visibles = Produit.objects.filter(categorie_id=2).filter(is_visible=True)    

    context['carousels'] = carousels
    context['actualites'] = actualites
    context['produits'] = produits
    context['produits_nonvie'] = produits_nonvie
    context['produits_nonvie_visibles'] = produits_nonvie_visibles
    context['produits_vie_visibles'] = produits_vie_visibles

    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful


    context['temoignages'] = temoignages

    context['products_keys'] = products_keys

    context['active_index'] = 'active_index'

    return render(request, "saar_website/index.html", context=context)


# def carousel(request, numero):

#     try:
#         context = {}
#         carousel = Caroussel.objects.get(pk=numero)

#         context['produits'] = produits

#         context['produits_nonvie'] = produits_nonvie
#         context['produits_vie'] = produits_vie
#         context['produits_takaful'] = produits_takaful

#         context['carousel'] = carousel
#         context['products_keys'] = products_keys
#         context['active_carousel'] = 'active_carousel'

#         return render(request, f"saar_website/carousel/carousel_{numero}.html", context=context)

#         # return render(request, f"saar_website/carousel/carousels.html", context=context)

#     #     return render(request, "saar_website/carousel/carousels.html", context=context)

#     except:
#         return render(request, "saar_website/404.html", context=context)


def carousel_chatbot(request):

    context = {}

    context['produits'] = produits

    context['produits_nonvie'] = produits_nonvie
    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful

    context['products_keys'] = products_keys
    context['active_carousel'] = 'active_carousel'

    return render(request, "saar_website/chatbot.html", context=context)



def test(request):

    return render(request, "saar_website/produits/test_design_auto.html")

def produit(request, numero):

    try:
        context = {}
        produit = Produit.objects.get(pk=numero)

        noms = [
        "AUTO","INCENDIE","VOYAGE","SANTE","CHANTIER","HABITATION",
        "INDIVIDUEL ACCIDENT","RESPONSABILITE CIVILE","MULTIRISQUE PROFESSIONNEL",
        "TRANSPORT"
            ]

        context['produit'] = produit
        context['produits'] = produits

        context['noms'] = noms

        context['produits_nonvie'] = produits_nonvie
        context['produits_vie'] = produits_vie
        context['produits_takaful'] = produits_takaful
        
        context['products_keys'] = products_keys
        context[f'active_produit{numero}'] = f'active_produit{numero}'

        return render(request, f"saar_website/produits/produit-{numero}.html", context=context)
    except:
        return render(request, "saar_website/404.html", context=context)    


def produit_detail(request, slug):

    context = {}
    produit = get_object_or_404(Produit, slug=slug)

    # print(produit.pk)

    detail_produit = DetailProduit.objects.filter(produit_id=produit.pk).first()
    formules = Formule.objects.filter(produit_id=produit.pk)
    garanties = Garantie.objects.filter(produit_id=produit.pk)

    context['produit'] = produit
    context['detail_produit'] = detail_produit
    context['formules'] = formules
    context['garanties'] = garanties

    context['produits'] = produits

    context['produits_nonvie'] = produits_nonvie
    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful

    context['products_keys'] = products_keys
    return render(request, "saar_website/produits/detail.html", context=context)



# class CarouselListView(ListView):
#     model = Caroussel
#     template_name = "saar_website/index.html"


# class CarouselDetailView(DetailView):
#     model = Caroussel
#     template_name = "saar_website/carousel/carousels.html"


def about(request):

    context = {}

    context['active_about'] = 'active_about'

    context['produits'] = produits

    context['produits_nonvie'] = produits_nonvie
    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful

    context['products_keys'] = products_keys

    return render(request, "saar_website/about_review.html", context=context)


def about_grp(request):

    context = {}

    context['products_keys'] = products_keys
    
    context['produits'] = produits

    context['produits_nonvie'] = produits_nonvie
    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful

    context['active_about_grp'] = 'active_about_grp'


    return render(request, "saar_website/about_grp_review.html", context=context)


def contact(request):

    context = {}

    context['produits'] = produits

    context['produits_nonvie'] = produits_nonvie
    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful

    context['active_contact'] = 'active_contact'

    context['products_keys'] = products_keys

    if request.method == 'POST':
        name = request.POST['name']
        from_email = request.POST['from_email']
        subject = request.POST['subject']
        message = request.POST['message']

        
        # Load the HTML template
        context_template = {'name': name, 'from_email': from_email, 'message':message}
        html_content = render_to_string('saar_website/email_template_review.html', context=context_template)

        email = EmailMultiAlternatives(subject=subject, body=f'{from_email} {name} : {message}', from_email=from_email, to=[settings.EMAIL_HOST_USER])
        email.attach_alternative(html_content, "text/html")
        email.send()

        # Load the HTML template
        message_user = "Votre requête a bien été reçue. Un de nos conseiller vous contacteras dans les plus brefs délais."
        context_user_template = {'name': name, 'from_email': from_email, 'message_user':message_user}
        html_user_content = render_to_string('saar_website/email_user_template.html', context=context_user_template)
        email_to_user = EmailMultiAlternatives(subject="Accusé de réception - SAAR CI", from_email=settings.DEFAULT_FROM_EMAIL, to=[from_email])
        email_to_user.attach_alternative(html_user_content, "text/html")
        email_to_user.send()

        # send_mail(subject=f'{subject}', message=f'{message} {name} {from_email}', from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.EMAIL_HOST_USER])

        message = f"Votre message a bien été reçu. Un mail de confirmation vous a été envoyé. Merci de faire confiance à SAAR Assurances Côte d'Ivoire."
        messages.success(request, message)

        return redirect('contact')


    return render(request, "saar_website/contact.html", context=context)


def agences(request):

    context = {}

    agences_abj = Agence.objects.filter(zone="ABIDJAN")
    agences_int = Agence.objects.filter(zone="INTERIEUR")

    nbre_agences_abj = Agence.objects.filter(zone="ABIDJAN").count()
    nbre_agences_int = Agence.objects.filter(zone="INTERIEUR").count()

    agent_generaux = AgentGeneral.objects.order_by('designation')

    context['produits'] = produits

    context['produits_nonvie'] = produits_nonvie
    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful

    context['agences_abj'] = agences_abj
    context['agences_int'] = agences_int

    context['nbre_agences_abj'] = nbre_agences_abj
    context['nbre_agences_int'] = nbre_agences_int

    context['agent_generaux'] = agent_generaux


    context['active_agences'] = 'active_agences'

    context['products_keys'] = products_keys

    return render(request, "saar_website/agences.html", context=context)



def reclamation(request):

    context = {}

    # context['active_agences'] = 'active_agences'

    # sinistre_form = SinistreForm()
    # context['sinistre_form'] = sinistre_form


    context['products_keys'] = products_keys

    context['produits'] = produits

    context['produits_nonvie'] = produits_nonvie
    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful

    if request.method == 'POST':

        # request.POST['constat_a']
        # request.POST['salarie_a']
        # request.POST['constat_b']
        # request.POST['salarie_a']

         # Champs du sinistre
        date_sinistre = request.POST['date_sinistre']
        lieu_sinistre = request.POST['lieu_sinistre']
        periode_du = request.POST['periode_du']
        periode_au = request.POST['periode_au']
        numero_police = request.POST['name']
        intervention = request.POST['intervention']

        # Champs de l'assuré
        nom_a = request.POST['nom_a']
        adresse_a = request.POST['adresse_a']
        phone_a = request.POST['phone_a']
        email_a = request.POST['email_a']

        # Champs du véhicule
        marque_a = request.POST['marque_a']
        imma_a = request.POST['imma_a']
        visite_du_a = request.POST['visite_du_a']
        visite_au_a = request.POST['visite_au_a']
        usage_a = request.POST['usage_a']

        # Champs du conducteur
        conducteur_a = request.POST['conducteur_a']
        adresse_conducteur_a = request.POST['adresse_conducteur_a']
        phone_conducteur_a = request.POST['phone_conducteur_a']
        profession_conducteur_a = request.POST['profession_conducteur_a']
        numero_permis = request.POST['numero_permis']
        date_delivrance_a = request.POST['date_delivrance_a']
        lieu_delivrance_a = request.POST['lieu_delivrance_a']
        categorie_a = request.POST['categorie_a']
        dure_a = request.POST['dure_a']

        # Champs pour les questions avec réponses Oui/Non
        constat_a = request.POST['constat_a']
        salarie_a = request.POST['salarie_a']

         # Récupérer les données du formulaire
        nom_b = request.POST['nom_b']
        adresse_b = request.POST['adresse_b']
        phone_b = request.POST['phone_b']
        email_b = request.POST['email_b']
        marque_b = request.POST['marque_b']
        imma_b = request.POST['imma_b']

        visite_du_b = request.POST.get('visite_du_b', '')
        if visite_du_b in ('', None, ' '):
            visite_du_b = None
        else:
            visite_du_b = datetime.strptime(visite_du_b, '%Y-%m-%d').date()

        visite_au_b = request.POST.get('visite_au_b', '')
        if visite_au_b in ('', None, ' '):
            visite_au_b = None
        else:
            visite_au_b = datetime.strptime(visite_du_b, '%Y-%m-%d').date()

        usage_b = request.POST['usage_b']

        conducteur_b = request.POST['conducteur_b']
        adresse_conducteur_b = request.POST['adresse_conducteur_b']
        phone_conducteur_b = request.POST['phone_conducteur_b']
        profession_conducteur_b = request.POST['profession_conducteur_b']
        numero_permis_b = request.POST['numero_permis_b']
        date_delivrance_b = request.POST['date_delivrance_b']

        if date_delivrance_b in ('', None, ' '):
            date_delivrance_b = None    
        else:
            date_delivrance_b = datetime.strptime(date_delivrance_b, '%Y-%m-%d').date()    


        lieu_delivrance_b = request.POST['lieu_delivrance_b']
        categorie_b = request.POST['categorie_b']
        dure_b = request.POST['dure_b'] if request.POST['dure_b'] else None
        constat_b = request.POST['constat_b']
        salarie_b = request.POST['salarie_b']

        circonstance = request.POST['circonstance']
        dommages = request.POST['dommages']


        sinistre = Sinistre(
            date_sinistre = date_sinistre,
            lieu_sinistre = lieu_sinistre,
            periode_du = periode_du,
            periode_au = periode_au,
            numero_police = numero_police,
            intervention = intervention,
            nom_a = nom_a,
            adresse_a = adresse_a,
            phone_a = phone_a,
            email_a = email_a,
            marque_a = marque_a,
            imma_a = imma_a,
            visite_du_a = visite_du_a,
            visite_au_a = visite_au_a,
            usage_a = usage_a,
            conducteur_a = conducteur_a,
            adresse_conducteur_a = adresse_conducteur_a,
            phone_conducteur_a = phone_conducteur_a,
            profession_conducteur_a = profession_conducteur_a,
            numero_permis = numero_permis,
            date_delivrance_a = date_delivrance_a,
            lieu_delivrance_a = lieu_delivrance_a,
            categorie_a = categorie_a,
            dure_a = dure_a,
            constat_a = constat_a,
            salarie_a = salarie_a,
            nom_b=nom_b,
            adresse_b=adresse_b,
            phone_b=phone_b,
            email_b=email_b,
            marque_b=marque_b,
            imma_b=imma_b,
            visite_du_b=visite_du_b,
            visite_au_b=visite_au_b,
            usage_b=usage_b,
            conducteur_b=conducteur_b,
            adresse_conducteur_b=adresse_conducteur_b,
            phone_conducteur_b=phone_conducteur_b,
            profession_conducteur_b=profession_conducteur_b,
            numero_permis_b=numero_permis_b,
            date_delivrance_b=date_delivrance_b,
            lieu_delivrance_b=lieu_delivrance_b,
            categorie_b=categorie_b,
            dure_b=dure_b,
            constat_b=constat_b,
            salarie_b=salarie_b,
            circonstance=circonstance,
            dommages=dommages
        )

        sinistre.save()

        if sinistre:
            context_template = {}

            context_template['date_sinistre'] = pd.to_datetime(date_sinistre)
            context_template['lieu_sinistre'] = lieu_sinistre
            context_template['periode_du'] = pd.to_datetime(periode_du)
            context_template['periode_au'] = pd.to_datetime(periode_au)
            context_template['numero_police'] = numero_police
            context_template['intervention'] = intervention
            context_template['nom_a'] = nom_a
            context_template['adresse_a'] = adresse_a
            context_template['phone_a'] = phone_a
            context_template['email_a'] = email_a
            context_template['marque_a'] = marque_a
            context_template['imma_a'] = imma_a
            context_template['visite_du_a'] = pd.to_datetime(visite_du_a)
            context_template['visite_au_a'] = pd.to_datetime(visite_au_a)
            context_template['usage_a'] = usage_a
            context_template['conducteur_a'] = conducteur_a
            context_template['adresse_conducteur_a'] = adresse_conducteur_a
            context_template['phone_conducteur_a'] = phone_conducteur_a
            context_template['profession_conducteur_a'] = profession_conducteur_a
            context_template['numero_permis'] = numero_permis
            context_template['date_delivrance_a'] = pd.to_datetime(date_delivrance_a)
            context_template['lieu_delivrance_a'] = lieu_delivrance_a
            context_template['categorie_a'] = categorie_a
            context_template['dure_a'] = dure_a
            context_template['constat_a'] = constat_a
            context_template['salarie_a'] = salarie_a
            context_template['nom_b'] = nom_b
            context_template['adresse_b'] = adresse_b
            context_template['phone_b'] = phone_b
            context_template['email_b'] = email_b
            context_template['marque_b'] = marque_b
            context_template['imma_b'] = imma_b
            context_template['visite_du_b'] = visite_du_b
            context_template['visite_au_b'] = visite_au_b
            context_template['usage_b'] = usage_b
            context_template['conducteur_b'] = conducteur_b
            context_template['adresse_conducteur_b'] = adresse_conducteur_b
            context_template['phone_conducteur_b'] = phone_conducteur_b
            context_template['profession_conducteur_b'] = profession_conducteur_b
            context_template['numero_permis_b'] = numero_permis_b
            context_template['date_delivrance_b'] = pd.to_datetime(date_delivrance_b)
            context_template['lieu_delivrance_b'] = lieu_delivrance_b
            context_template['categorie_b'] = categorie_b
            context_template['dure_b'] = dure_b
            context_template['constat_b'] = constat_b
            context_template['salarie_b'] = salarie_b
            context_template['circonstance'] = circonstance
            context_template['dommages'] = dommages

            date_actuel = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                # html_content = render_to_string('saar_website/template_sinistre.html', context=context_template)

            html_string = render_to_string('saar_website/template_sinistre2.html', context=context_template)
            #pdf_file = HTML(string=html_string).write_pdf(stylesheets=[CSS(settings.STATIC_ROOT / 'css/style.css'), CSS(settings.STATIC_ROOT / 'css/bootstrap.min.css')])
            pdf_file = HTML(string=html_string).write_pdf(stylesheets=[CSS(settings.STATICFILES_DIRS[0] / 'css/style_pdf.css'), CSS(settings.STATIC_ROOT / 'css/style.css'), CSS(settings.STATIC_ROOT / 'css/bootstrap.min.css')])

            email = EmailMessage(subject=f'DECLARATION SINISTRE AUTOMOBILE {date_actuel}', body=f"Veuillez trouver ci-joint le PDF de déclaration de sinistre de l'assuré {nom_a}, numéro de police {numero_police} à la date du {date_actuel}.", from_email='saarci.assurance@gmail.com', to=['saarci.assurance@gmail.com'])
            email.attach('declaration_sinistre.pdf', pdf_file, 'application/pdf')
            
            email.send()


              # Load the HTML template
            message_user = "Votre réclamation a bien été reçu, un de nos conseiller vous contacteras dans un bref délai. Merci de nous faire confiance."
            context_user_template = {'name': nom_a, 'email': email_a, 'message_user':message_user}
            html_user_content = render_to_string('saar_website/email_user_template.html', context=context_user_template)
            email_to_user = EmailMultiAlternatives(subject="Accusé de réception - SAAR CI", from_email=settings.DEFAULT_FROM_EMAIL, to=[email_a])
            email_to_user.attach_alternative(html_user_content, "text/html")
            email_to_user.send()

            message = f"Votre réclamation a bien été enregistré et transmis au service sinistre, un de nos gestionnaire sinistre vous contactera dans un bref délai pour finaliser votre procédure."
            messages.success(request, message)

            return redirect('reclamation')
            #return render(request, 'saar_website/template_sinistre.html', context=context_template)

            # response = HttpResponse(pdf_file, content_type="application/pdf")
            # response['Content-Disposition'] = 'filename="test.pdf"'

            # return response

        else:
            message = f"Aucun enregistrement n'a été fait dans la base."
            messages.warning(request, message)

            return redirect('reclamation')


    return render(request, "saar_website/reclamation.html", context=context)



def valeurs(request):

    context = {}

    # context['active_agences'] = 'active_agences'

    context['products_keys'] = products_keys

    context['produits'] = produits

    context['produits_nonvie'] = produits_nonvie
    context['produits_vie'] = produits_vie
    context['produits_takaful'] = produits_takaful

    context['active_valeurs'] = 'active_valeurs'

    return render(request, "saar_website/valeurs_review.html", context=context)



