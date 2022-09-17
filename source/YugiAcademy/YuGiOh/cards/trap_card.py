from django.db import models

from YuGiOh.models import Card


class TrapCard(Card):
    type = models.CharField(max_length=20)

    def related_query_name(self):
        return 'trap_card'
