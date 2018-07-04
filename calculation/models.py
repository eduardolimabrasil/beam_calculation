from django.db import models

class Calculation(models.Model):
    force = models.FloatField()
    distance = models.FloatField()
    allowable_stress = models.FloatField()
    unit_force = models.CharField(max_length=5)
    unit_distance = models.CharField(max_length=5)
    unit_allowable_stress = models.CharField(max_length=5)