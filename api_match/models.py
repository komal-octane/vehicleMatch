from django.db import models

# Create your models here.
class VehicleMatch(models.Model):
    model_name = models.CharField("Model", max_length=500)
    make = models.CharField("Make", max_length=500)
    trim = models.CharField("Model_trim", max_length=250)

    def __str__(self):
        return self.model_name + self.make + self.trim