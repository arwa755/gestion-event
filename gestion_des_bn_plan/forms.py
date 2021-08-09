from django.forms import ModelForm

from gestion_des_bn_plan.models import bonplan



class bonplanForm(ModelForm):
    class Meta:
        model = bonplan
        fields = ('téléphone', 'email', 'adresse')
