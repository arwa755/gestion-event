from django.shortcuts import render, get_object_or_404, redirect
from gestion_des_bn_plan.forms import bonplanForm
# Create your views here.
from gestion_des_bn_plan.models import bonplan


def index(request):
    bonplans = bonplan.objects.all().order_by('adresse') #Obtenez de la valeur
    return render(request, 'bonplan/index.html', {'bonplan':bonplans}) #Passer une valeur au modèle


# Nouveau et modifier

def edit(request, id=None, bonplan=None):
    if id:
        bonplan= get_object_or_404(bonplan, ID=id)
    else:
        bonplan= bonplan()

    # Au POST (lorsque le bouton d'enregistrement est enfoncé, que ce soit nouveau ou modifier)
    if request.method == 'POST':
        # Générer un formulaire
        form = bonplanForm(request.POST, instance=bonplan)
        if form.is_valid():  # Enregistrer si la validation est OK
            bonplan= form.save(commit=False)
            bonplan.save()
            return redirect('crud:index')
    else:  # Au moment de GET (générer un formulaire)
        form = bonplanForm(instance=bonplan)

    # Afficher un nouvel écran / modifier l'écran
    return render(request, 'bonplan/edit.html', dict(form=form, id=id))




#supprimer
def delete(request, id, bonplan=None):
    bonplan= get_object_or_404(bonplan, ID=id)
    bonplan.delete()
    return redirect('crud:index')


