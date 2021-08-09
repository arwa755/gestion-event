from django.db import models
from django.db.models import Model

# TABLE PUBLICATION
class publication(models.Model):
    description = models.CharField(max_length=300, null=True)
    image = models.ImageField(unique=True, null=True)
    categorie = models.CharField(max_length=50, null=True)
    tags = models.CharField(max_length=300, null=True)
    ref = models.CharField(max_length=50,unique=True, null=True)
    title = models.CharField(max_length=50,unique=True, null=True)

    def __str__(self):
        return self.id
#table bon_plan
class bonplan (publication):
     tel = models.CharField(max_length=12,unique=True)
     email = models.EmailField(blank=True,unique=True)
     adresse = models.TextField(unique=True)







#








