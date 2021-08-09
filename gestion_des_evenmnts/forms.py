from django.forms import ModelForm

from gestion_des_evenmnts.models import evenement


class EvenemtForm(ModelForm):
	class Meta:
		model = evenement
		fields = ('lieu exacte' ,'date' ,' nombre placesDisponible')