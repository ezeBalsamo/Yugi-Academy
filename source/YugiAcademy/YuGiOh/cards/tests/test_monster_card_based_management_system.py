import pytest

from YuGiOh.cards import CardManagementSystem, MonsterCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound, \
                        assert_is_empty, assert_the_only_one_in, \
                        with_the_only_one_in


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


def celtic_guardian():
    return MonsterCard.named(name='Celtic Guardian',
                             race='Warrior',
                             attribute='Earth',
                             level=4,
                             attack=1400,
                             defense=1200,
                             description='An elf who learned to wield a sword, '
                                         'he baffles enemies with lightning-swift attacks.')


def assert_monster_card_was_updated(monster_card, updated_monster_card, managed_monster_card):
    assert managed_monster_card == monster_card
    assert managed_monster_card.name == updated_monster_card.name
    assert managed_monster_card.race == updated_monster_card.race
    assert managed_monster_card.attribute == updated_monster_card.attribute
    assert managed_monster_card.level == updated_monster_card.level
    assert managed_monster_card.attack == updated_monster_card.attack
    assert managed_monster_card.defense == updated_monster_card.defense
    assert managed_monster_card.description == updated_monster_card.description


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
        
    def test_purge_monster_card(self):
        monster_card = dark_magician()
        self.system.store_monster_card(monster_card)
        assert_the_only_one_in(self.system.monster_cards(), monster_card)
        self.system.purge_monster_card(monster_card)
        assert_is_empty(self.system.monster_cards())
        
    def test_cannot_purge_monster_card_not_found(self):
        monster_card = dark_magician()
        self.system.store_monster_card(monster_card)
        self.system.purge_monster_card(monster_card)
        with pytest.raises(DataInconsistencyFound) as exception_info:
            self.system.purge_monster_card(monster_card)
        assert exception_info.message_text() == 'Dark Magician was expected to be found, but it was not.'
        assert_is_empty(self.system.monster_cards())
        
    def test_update_monster_card(self):
        monster_card = dark_magician()
        updated_monster_card = celtic_guardian()
        self.system.store_monster_card(monster_card)
        self.system.update_monster_card_with(monster_card, updated_monster_card)
        with_the_only_one_in(self.system.monster_cards(),
                             lambda managed_monster_card: 
                             assert_monster_card_was_updated(monster_card, updated_monster_card, managed_monster_card))
