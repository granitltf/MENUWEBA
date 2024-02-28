from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BoireForm
from .models import Boire


# Create your views here.
def liste_boisson(request):
    return render(request,'boire/liste_boissons.html')

def ajouter_boissons(request):
    form = BoireForm()
    if request.method == 'POST':
        form = BoireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request,'boire/ajouter_boisson.html',context)

def modifier_boissons(request,pk):
    boisson = Boire.objects.get(id=pk)
    form = BoireForm(instance=boisson)
    if request.method == 'POST':
        form = BoireForm(request.POST,instance=boisson)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request,'boire/ajouter_boisson.html',context)

def supprimer_boissons(request,pk):
    boisson = Boire.objects.get(id=pk)
    if request.method == 'POST':
        boisson.delete()
        return redirect('/')
    context={'item':boisson}
    return render(request,'boire/supprimer_boissons.html',context)