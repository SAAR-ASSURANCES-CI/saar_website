from django.shortcuts import render

from administration.models import Caroussel, Actualite

from django.views.generic import ListView, DetailView


def index(request):

    context = {}

    # Carousel

    carousels = Caroussel.objects.all()
    actualites = Actualite.objects.all()

    context['carousels'] = carousels
    context['actualites'] = actualites

    context['assurance_auto'] = "Votre sécurité est notre priorité absolue sur la route. Avec notre assurance automobile, vous bénéficiez d'une protection fiable et d'un service attentionné à chaque étape. 𝐀𝐒𝐒𝐔𝐑𝐀𝐍𝐂𝐄 𝐌𝐎𝐓𝐎  : À partir de 10 000 FCFA / Année. 𝑨̀ 𝑵𝒐𝒕𝒆𝒓 : 𝑳𝒆𝒔 𝒑𝒓𝒊𝒎𝒆𝒔 𝒏𝒆 𝒔𝒐𝒏𝒕 𝒑𝒂𝒔 𝒇𝒊𝒙𝒆s : La prime à payer dépendra de l'usage de votre véhicule, de  l'énergie et de la puissance ou le tonnage."
    context['assurance_sante'] = "SAAR SANTE est une belle compilation de trois risques : maladie, assistance et évacuation sanitaire. Il s'agit d'un '3 en 1', au choix du client. SAAR SANTE garantit, dans les limites du plafond de remboursement, la prise en charge des risques de voyage suivants :"
    context['assurance_voyage'] = "Prévoyez-vous un voyage et recherchez-vous une assurance fiable pour vous accompagner ? Optez pour #Saar_Assistance_Voyage pour garantir votre sécurité et voyager l'esprit tranquille, que ce soit vers les pays de l'espace Schengen ou ailleurs dans le monde. Profitez d'une couverture complète pour voyager en toute tranquillité. 𝑷𝒓𝒊𝒔𝒆 𝒆𝒏 𝒄𝒉𝒂𝒓𝒈𝒆 𝒂̀ 𝒍’𝒆́𝒕𝒓𝒂𝒏𝒈𝒆𝒓 𝒅𝒆𝒔 𝒇𝒓𝒂𝒊𝒔 𝒎𝒆́𝒅𝒊𝒄𝒂𝒖𝒙 𝒅’𝒖𝒓𝒈𝒆𝒏𝒄𝒆 𝒆𝒏 𝒄𝒂𝒔 𝒅𝒆 𝒎𝒂𝒍𝒂𝒅𝒊𝒆  𝒂̀ 𝒄𝒐𝒏𝒄𝒖𝒓𝒓𝒆𝒏𝒄𝒆 𝒅𝒆 19 740 000 𝑭𝑪𝑭𝑨. 𝑰𝒏𝒅𝒆𝒎𝒏𝒊𝒕𝒆́ 𝒄𝒐𝒎𝒑𝒍𝒆́𝒎𝒆𝒏𝒕𝒂𝒊𝒓𝒆 𝒆𝒏 𝒄𝒂𝒔 𝒅𝒆 𝒑𝒆𝒓𝒕𝒆 𝒅𝒆 𝒗𝒐𝒔 𝒃𝒂𝒈𝒂𝒈𝒆𝒔. "
    context['individuelle_accidents'] = "Que ce soit dans votre sphère personnelle ou professionnelle, les accidents sont des réalités auxquelles personne n'est à l'abri, avec des conséquences potentiellement graves pour vous et vos proches. 𝘿𝙀𝙏𝘼𝙄𝙇𝙎 𝘿𝙀 𝙇'𝙊𝙁𝙁𝙍𝙀 : Protégez votre famille et vous-même en optant pour l'assurance Individuelle Accidents de SAAR Assurances Côte d'Ivoire. Cette couverture complète inclut la protection contre les risques de décès, d'invalidité permanente et les frais médicaux, assurant le versement d'un capital préalablement choisi."
    context['assurance_transport'] = "𝐋'𝐚𝐬𝐬𝐮𝐫𝐚𝐧𝐜𝐞 𝐓𝐫𝐚𝐧𝐬𝐩𝐨𝐫𝐭  est  indispensable pour toute entreprise impliquée dans l'importation et/ou l'exportation de biens, offrant une couverture contre les risques courants lors des voyages par mer, air ou terre. En Côte d'Ivoire, cette assurance est désormais obligatoire pour toutes les marchandises importées depuis la mise en vigueur du Décret d'application n°2007-479 du 16 mai 2007. SAAR ASSURANCES CÔTE D'IVOIRE  met à votre disposition son expertise dans ce domaine pour répondre à vos besoins."
    context['assurance_caution'] = "Avec la Caution SAAR, j'optimise ma trésorerie. Les cautions comportent des risques liés à la défaillance du client. A la Saar, l'obtention d'une caution est basée sur une analyse minutieuse des capacités techniques, organisationnelles et financières des demandeurs."
    context['assurance_habitation'] = "𝐋'𝐚𝐬𝐬𝐮𝐫𝐚𝐧𝐜𝐞 𝐡𝐚𝐛𝐢𝐭𝐚𝐭𝐢𝐨𝐧 de la SAAR assure la protection de votre domicile et de vos biens contre les dommages matériels ou corporels causés par un sinistre. Notre 𝐚𝐬𝐬𝐮𝐫𝐚𝐧𝐜𝐞 𝐦𝐮𝐥𝐭𝐢𝐫𝐢𝐬𝐪𝐮𝐞 𝐡𝐚𝐛𝐢𝐭𝐚𝐭𝐢𝐨𝐧 offre une gamme complète de garanties pour vous protéger contre les risques les plus courants, tels que 𝐥'𝐢𝐧𝐜𝐞𝐧𝐝𝐢𝐞, 𝐥𝐞𝐬 𝐝𝐞́𝐠𝐚̂𝐭𝐬 𝐝𝐞𝐬 𝐞𝐚𝐮𝐱, 𝐥𝐞𝐬 𝐛𝐫𝐢𝐬 𝐝𝐞 𝐠𝐥𝐚𝐜𝐞, 𝐥𝐞 𝐯𝐨𝐥... en tant que propriétaire ou occupant. Notre contrat couvre votre maison, appartement ou immeuble, ainsi que vos équipements, membres de votre foyer et vous-même. En cas de dommages ou de préjudices causés à un tiers, notre assurance vous indemnise pour les pertes subies ou les frais engagés."
    context['saar_takaful'] = "Saar TAKAFUL est une forme d'assurance basée sur l'entraide et la solidarité entre des personnes pour faire face à divers risques. Protégez votre famille, vos biens et votre responsabilité avec nos polices d'assurance conformes aux principes islamiques."
    context['risques_divers'] = "Découvrez nos solutions d'assurances Incendie, Responsabilités Civiles, Risques techniques et autres riques.La mission fondamentale de l’assurance est d’apporter aux hommes la sécurité dont ils ont besoin pour affronter le quotidien et avoir confiance en l’avenir. Chez SAAR, nous vous offrons efficacement l’accompagnement qu’il faut face à vos besoins de sécurité et celui de vos biens."
    

    context['actualite_1'] = "Ce mercredi 1er Mai s'est tenue, à l'hotel FAMILLE MONDIALE, la célébration de la fête du travail réunissant tous les employés de la SAAR Côte d'Ivoire."
    context['actualite_2'] = "Du 𝟎𝟖 𝐚𝐮 𝟏𝟎 𝐌𝐚𝐫𝐬, la 𝐒𝐨𝐜𝐢𝐞́𝐭𝐞́ 𝐀𝐟𝐫𝐢𝐜𝐚𝐢𝐧𝐞 𝐝'𝐀𝐬𝐬𝐮𝐫𝐚𝐧𝐜𝐞𝐬 𝐞𝐭 𝐝𝐞 𝐑𝐞́𝐚𝐬𝐬𝐮𝐫𝐚𝐧𝐜𝐞𝐬 𝐝𝐞 𝐂𝐨̂𝐭𝐞 𝐝'𝐈𝐯𝐨𝐢𝐫𝐞 (𝐒𝐀𝐀𝐑 𝐂𝐈) a organisé 𝐮𝐧𝐞 𝐬𝐞́𝐚𝐧𝐜𝐞 𝐝𝐞 𝐭𝐫𝐚𝐯𝐚𝐢𝐥 à 𝗖𝗮𝗻𝗻𝗮𝗻 𝗛𝗶𝗹𝗹𝘀, 𝗬𝗮𝗺𝗼𝘂𝘀𝘀𝗼𝘂𝗸𝗿𝗼. Dans un cadre professionnel empreint de sérieux et de rigueur, ces journées ont été marquées par une intense réflexion sur l'avenir de l'assurance."
    context['actualite_3'] = "ce samedi 07 Octobre, nous avons organisé avec le Club des Hommes d'affaires musulmans de Côte d'Ivoire CHAMCI, un déjeuner de présentation de nos offres SAAR_TAKAFUL, notre gamme de produits d'assurance conforme à la Sharia. Après la présentation faite par monsieur Loïc Armel KENGNE WAFO,LLB,MBA,ACCPA , la centaine de Dirigeants d'entreprises s'est dite satisfaite de cette innovation."
    
    return render(request, "saar_website/index.html", context=context)


def carousel(request, numero):

    try:
        context = {}
        carousel = Caroussel.objects.get(pk=numero)

        context['carousel'] = carousel
        return render(request, f"saar_website/carousel/carousels.html", context=context)
    except:
        return render(request, "saar_website/404.html")
    

# class CarouselListView(ListView):
#     model = Caroussel
#     template_name = "saar_website/index.html"


# class CarouselDetailView(DetailView):
#     model = Caroussel
#     template_name = "saar_website/carousel/carousels.html"



