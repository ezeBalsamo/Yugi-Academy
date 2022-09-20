import pytest

from YuGiOh.cards import CardManagementSystem, MonsterCard
from assertions import assert_is_empty, assert_the_only_one_in


def dark_magician():
    return MonsterCard.named(name='Dark Magician',
                             race='Spellcaster',
                             attribute='Dark',
                             level=7,
                             attack=2500,
                             defense=2100,
                             description='The ultimate wizard in terms of attack and defense.')


@pytest.mark.django_db
class TestCardManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.system = CardManagementSystem()

    def test_store_monster_card(self):
        assert_is_empty(self.system.monster_cards())
        monster_card = dark_magician()
        self.system.store_monster_card(monster_card)
        assert_the_only_one_in(self.system.monster_cards(), monster_card)
