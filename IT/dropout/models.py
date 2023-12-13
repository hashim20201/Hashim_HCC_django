from django.db import models

# Create your models here.

class people(models.Model):
    name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    place_of_birth=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name+' '+self.company


