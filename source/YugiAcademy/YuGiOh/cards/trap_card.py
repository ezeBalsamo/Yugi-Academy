from django.db import models

from .card import Card
from assertions import enforce_not_blank


class TrapCard(Card):
    type = models.CharField(max_length=20)

    @classmethod
    def named(cls, name: str, type: str, description: str):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_not_blank(description, "Description")

        return cls(name=name, type=type, description=description)

    def related_query_name(self):
        return 'trap_card'
