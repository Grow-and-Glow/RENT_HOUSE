from django.shortcuts import render
from .models import House, HouseStatus


# ==================================maison=========================================
def home(request):
    houses = House.objects.filter(status=HouseStatus.PUBLISHED).select_related("quarter")[:6]
    return render(request, 'index.html', {'houses': houses})

def supprimer_maison(request):
    return render(request=request, template_name='public/maison/supprimer_maison.html', context={})

def detail_maison(request):
    return render(request=request, template_name='public/maison/detail_maison.html', context={})

def annonce_maison(request):
    return render(request=request, template_name='public/maison/annonce_maison.html', context={})

# ===============================authentification=====================================
def inscription(request):
    return render(request=request, template_name='public/authentification/inscription.html', context={})


# Base app

def app(request):
    return render(
        request= request,
        template_name= "baseApp.html",
        context={}
    )