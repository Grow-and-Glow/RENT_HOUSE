from django.shortcuts import render


# ==================================maison=========================================
def home(request):
    return render(request, 'public/home.html')

def ajouter_maison(request):
    return render(request=request, template_name='public/maison/ajouter_maison.html', context={})

def supprimer_maison(request):
    return render(request=request, template_name='public/maison/supprimer_maison.html', context={})

def detail_maison(request):
    return render(request=request, template_name='public/maison/detail_maison.html', context={})

def annonce_maison(request):
    return render(request=request, template_name='public/maison/annonce_maison.html', context={})

# ===============================authentification=====================================
def inscription(request):
    return render(request=request, template_name='public/authentification/inscription.html', context={})