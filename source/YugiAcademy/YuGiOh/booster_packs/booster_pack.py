from django.db import models

from assertions import enforce_not_blank


class BoosterPack(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10)
    release_date = models.DateField()

    @classmethod
    def named(cls, name, code, release_date):
        enforce_not_blank(name, "Name")

    def __str__(self):
        return self.name
