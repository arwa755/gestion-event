from django.db import models
from django.db.models import Model
from gestion_des_bn_plan.models import publication



# table evenmnts
class evenement (publication):
    lieu = models.CharField('lieu exacte',max_length=300)
    date = models.DateTimeField()
    placesDispo = models.PositiveIntegerField('nbre de pLace disponible')
