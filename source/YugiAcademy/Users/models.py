from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=25)
    description = models.DateField(null=True, blank=True)
    web_site = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self:name} - Email: {self.email}"
