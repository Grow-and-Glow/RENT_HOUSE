from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    # =======================urls pour Maison===========================

    path(route='maison/ajouter_maison', view=views.ajouter_maison, name='ajouter-maison'),
    path(route='maison/detail_maison', view=views.detail_maison, name='detail-maison'),
    path(route='maison/supprimer_maison', view=views.supprimer_maison, name='supprimer-maison'),
    path(route='maison/annonce_maison', view=views.annonce_maison, name='annonce-maison'),

    # ========================urls pour authentification ==================
    path(route='authentification/inscription', view=views.inscription, name='inscription'),

    # Base App
    path(route="app/",view=views.app, name="baseApp")
]