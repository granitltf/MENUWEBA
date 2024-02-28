from django.shortcuts import render, redirect
from .forms import CommandeForm


from .models import Commande

def liste_commande(request):
    return render(request,'commande/liste_commande.html')

def ajouter_commande(request):
    form = CommandeForm(request)
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            manger_id = form.cleaned_data['manger']
            boire_id = form.cleaned_data['boire']
            if not Commande.objects.filter(manger_id=manger_id, boire_id=boire_id).exists():
                form.save()
                return redirect('/')
            else:
                form.add_error(None, 'Cette commande existe déjà.')
    else:
        form = CommandeForm()
    context = {'form':form}
    return render(request,'commande/ajouter_commande.html',context)