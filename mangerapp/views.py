from django.shortcuts import render, redirect
from django.http import HttpResponse
from boireapp.models import Boire
from mangerapp.models import Manger
from .models import Manger
from .forms import MangerForm
from commande.models import Commande


# Create your views here.
def home(request):
    commande = Commande.objects.all()
    boison_filter = Boire.objects.filter(commande__in=commande)
    boire = Boire.objects.all()
    manger = Manger.objects.all()
    context = {'manger': manger, 'boire': boire, 'commande': commande}
    return render(request, 'manger/acceuil.html', context)


def ajouter_plats(request):
    form = MangerForm()
    if request.method == 'POST':
        form = MangerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'manger/ajouter_plats.html', context)


def modifier_plats(request, pk):
    plat = Manger.objects.get(id=pk)
    form = MangerForm(instance=plat)
    if request.method == 'POST':
        form = MangerForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'manger/ajouter_plats.html', context)


def supprimer_plats(request, pk):
    plat = Manger.objects.get(pk=pk)
    if request.method == 'POST':
        plat.delete()
        return redirect('/')
    context = {'item': plat}
    return render(request, 'manger/supprimer_plats.html', context)
