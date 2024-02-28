from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_boisson),
    path('ajout_boisson/',views.ajouter_boissons, name='ajout_boisson'),
    path('modifier_boisson/<str:pk>', views.modifier_boissons, name='modifier_boisson'),
    path('supprimer_boisson/<str:pk>', views.supprimer_boissons, name='supprimer_boisson'),
]
