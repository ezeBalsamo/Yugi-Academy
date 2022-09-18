from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=8000)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
