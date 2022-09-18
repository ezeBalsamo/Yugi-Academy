from django.db import models

from datetime import datetime

from assertions import enforce_not_blank


class BoosterPack(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10)
    release_date = models.DateField()

    @classmethod
    def named(cls, name: str, code: str, release_date: datetime):
        enforce_not_blank(name, "Name")
        enforce_not_blank(code, "Code")

        return cls(name=name, code=code, release_date=release_date)

    def __str__(self):
        return self.name
