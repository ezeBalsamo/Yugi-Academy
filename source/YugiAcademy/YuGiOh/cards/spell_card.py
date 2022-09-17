from django.db import models

from YuGiOh.models import Card
from assertions.assertions import enforce_not_blank


class SpellCard(Card):
    type = models.CharField(max_length=20)

    @classmethod
    def named(cls, name: str, type: str, description: str):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_not_blank(description, "Description")

        return cls(name=name, type=type, description=description)

    def related_query_name(self):
        return 'spell_card'
