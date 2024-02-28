from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='acceuil'),
    path('ajout_plat/',views.ajouter_plats, name='ajout_plat'),
    path('modifier_plat/<str:pk>', views.modifier_plats, name='modifier_plat'),
    path('supprimer_plat/<int:pk>', views.supprimer_plats, name='supprimer_plat'),
]
