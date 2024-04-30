from django.shortcuts import render


def index(request):
    return render(request, "saar_website/index.html")