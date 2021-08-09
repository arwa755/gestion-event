from django.shortcuts import render, get_object_or_404, redirect  # ajouter à
from gestion_des_evenmnts.models import evenement
from gestion_des_evenmnts.forms import EvenemtForm


#liste des evenemts

def index(request):
    evenements = evenement.objects.all().order_by('id') #Obtenez de la valeur
    return render(request, 'evenement/index.html', {'evenemts':evenements})
    #Passer une valeur au modèle

# Nouveau et modifier

def edit(request, id=None, evenement=None):
    if id:
        evenement = get_object_or_404(evenement, ID=id)
    else:
        evenement= evenement()

    # Au POST (lorsque le bouton d'enregistrement est enfoncé, que ce soit nouveau ou modifier)
    if request.method == 'POST':
        # Générer un formulaire
        form = EvenemtForm(request.POST, instance=evenement)
        if form.is_valid():  # Enregistrer si la validation est OK
            evenement= form.save(commit=False)
            evenement.save()
            return redirect('crud:index')
    else:  # Au moment de GET (générer un formulaire)
        form = EvenemtForm(instance=evenement)

    # Afficher un nouvel écran / modifier l'écran
    return render(request, 'evenemnt/edit.html', dict(form=form, id=id))

def delete(request, id, evenement=None):
    evenement= get_object_or_404(evenement, ID=id)
    evenement.delete()
    return redirect('crud:index')


