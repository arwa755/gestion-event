
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from gestion_news.forms import actualiteForm
from gestion_news.models import actualite


def index(request):
    actualites= actualite.objects.all().order_by('date')  # Obtenez de la valeur
    return render(request, 'actualite/index.html', {'actualite' :actualites})  # Passer une valeur au modèle


# Nouveau et modifier

def edit(request, id=None, actualite=None):
    if id:
        actualite  = get_object_or_404(actualite, ID=id)
    else:
        actualite= actualite()

    # Au POST (lorsque le bouton d'enregistrement est enfoncé, que ce soit nouveau ou modifier)
    if request.method == 'POST':
        # Générer un formulaire
        form = actualiteForm(request.POST, instance=actualite)
        if form.is_valid():  # Enregistrer si la validation est OK
            actualite= form.save(commit=False)
            actualite.save()
            return redirect('crud:index')
    else:  # Au moment de GET (générer un formulaire)
        form = actualiteForm(instance=actualite)

    # Afficher un nouvel écran / modifier l'écran
    return render(request, 'actualite/edit.html', dict(form=form, id=id))


# supprimer
def delete(request, id, actualite=None):
    actualite= get_object_or_404(actualite, ID=id)
    actualite.delete()
    return redirect('crud:index')
