from django.db import models

from datetime import date

from assertions import enforce_not_blank


class BoosterPack(models.Model):
    type_description = 'booster pack'
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10)
    release_date = models.DateField()

    @classmethod
    def named(cls, name: str, code: str, release_date: date):
        enforce_not_blank(name, "Name")
        enforce_not_blank(code, "Code")

        return cls(name=name, code=code, release_date=release_date)

    def __str__(self):
        return self.name

    def synchronize_with(self, booster_pack):
        self.name = booster_pack.name
        self.code = booster_pack.code
        self.release_date = booster_pack.release_date
