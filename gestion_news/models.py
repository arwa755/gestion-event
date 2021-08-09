from django.db import models
from django.db.models import Model
from gestion_des_bn_plan.models import publication


class actualite(publication):
    date = models.DateTimeField()
