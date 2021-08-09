from django.forms import ModelForm

from gestion_news.models import actualite


class actualiteForm(ModelForm):
    class Meta:
        model = actualite
        fields = 'date de l"actualité'
