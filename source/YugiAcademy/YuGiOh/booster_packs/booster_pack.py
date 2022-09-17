from django.db import models


class BoosterPack(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name
