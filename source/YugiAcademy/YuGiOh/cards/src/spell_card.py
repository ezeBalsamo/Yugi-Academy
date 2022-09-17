from django.db import models

from YuGiOh.models import Card

from utils.src.instance_creation_failed import InstanceCreationFailed


def enforce_not_blank(string, name):
    if not string.strip():
        raise InstanceCreationFailed(f'{name} must not be blank.')


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
