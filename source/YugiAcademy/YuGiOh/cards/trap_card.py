from django.db import models

from YuGiOh.models import Card
from assertions import enforce_not_blank


class TrapCard(Card):
    type = models.CharField(max_length=20)

    @classmethod
    def named(cls, name: str, type: str, description: str):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")

    def related_query_name(self):
        return 'trap_card'
