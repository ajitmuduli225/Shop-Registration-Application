from django.db import models

# Create your models here.

class Shop(models.Model):
    name=models.CharField(max_length=60)
    latitude=models.FloatField()
    longitude=models.FloatField()

    def __str__(self):
        return self.name