import pytest

from YuGiOh.cards import CardManagementSystem, MonsterCard
from assertions import SystemRestrictionInfringed, assert_is_empty, assert_the_only_one_in


def dark_magician():
    return MonsterCard.named(name='Dark Magician',
                             race='Spellcaster',
                             attribute='Dark',
                             level=7,
                             attack=2500,
                             defense=2100,
                             description='The ultimate wizard in terms of attack and defense.')


def monster_card_named(name):
    return MonsterCard.named(name=name,
                             race='Warrior',
                             attribute='Earth',
                             level=4,
                             attack=1400,
                             defense=1200,
                             description='An elf who learned to wield a sword, '
                                         'he baffles enemies with lightning-swift attacks.')


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

    def test_cannot_store_monster_card_when_there_is_one_with_same_name(self):
        monster_card = dark_magician()
        another_monster_card = monster_card_named(monster_card.name)
        self.system.store_monster_card(monster_card)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.store_monster_card(another_monster_card)
        assert exception_info.message_text() == 'There is already a monster card named Dark Magician.'
        assert_the_only_one_in(self.system.monster_cards(), monster_card)
