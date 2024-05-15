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

from .views import about, agences, contact, index, carousel, produit

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),

    path('carousels/<str:numero>/', carousel, name='carousel'),

    path('produits/<str:numero>/', produit, name='produit'),

    path('about/', about, name='about'),

    path('contact/', contact, name='contact'),

    path('agences/', agences, name='agences'),

    # path('', CarouselListView.as_view(), name="carousel_detail"),
    # path('carousel/<slug:slug>', CarouselDetailView.as_view() , name="carousel_detail"),

    path('administration/', include('administration.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


