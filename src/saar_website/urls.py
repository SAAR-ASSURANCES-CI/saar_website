"""
URL configuration for saar_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#from .views import index, carousel, CarouselListView, CarouselDetailView

#from .views import about, agences, contact, index, produit, about_grp, produit_detail, reclamation, valeurs, carousel_chatbot, test
from .views import about, agences, contact, index, about_grp, reclamation, valeurs, carousel_chatbot, test

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),

    # path('carousels/<str:numero>/', carousel, name='carousel'),

    path('carousels/chatbot/', carousel_chatbot, name='carousel_chatbot'),

    # path('produits/<str:numero>/', produit, name='produit'),

    # path("produit-view/<slug:slug>/", produit_detail, name="produit_detail"),


    path('about/', about, name='about'),

    path('about-group/', about_grp, name='about_grp'),


    path('contact/', contact, name='contact'),

    path('agences/', agences, name='agences'),

    path('valeurs/', valeurs, name='valeurs'),

    path('reclamation/', reclamation, name='reclamation'),

    path('test_page/', test, name='test'),


    # path('', CarouselListView.as_view(), name="carousel_detail"),
    # path('carousel/<slug:slug>', CarouselDetailView.as_view() , name="carousel_detail"),

    path('administration/', include('administration.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Pour servir les fichiers statiques en développement avec DEBUG=False
# if settings.DEBUG == False:  # Forcez temporairement
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


