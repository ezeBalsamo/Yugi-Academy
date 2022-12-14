import pytest
from django.db.models.fields.files import ImageFieldFile, FileField

from YuGiOh.cards import CardManagementSystem, MonsterCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound, \
    assert_is_empty, assert_the_only_one_in, \
    with_the_only_one_in, \
    assert_collections_have_same_elements


def card_image():
    return ImageFieldFile(instance=None, field=FileField(), name='cards/monster_cards/victory.jpg')


def dark_magician():
    return MonsterCard.named(name='Dark Magician',
                             type='Normal',
                             race='Spellcaster',
                             attribute='Dark',
                             level=7,
                             attack=2500,
                             defense=2100,
                             description='The ultimate wizard in terms of attack and defense.',
                             image=card_image())


def monster_card_named(name):
    return MonsterCard.named(name=name,
                             type='Normal',
                             race='Warrior',
                             attribute='Earth',
                             level=4,
                             attack=1400,
                             defense=1200,
                             description='An elf who learned to wield a sword, '
                                         'he baffles enemies with lightning-swift attacks.',
                             image=card_image())


def celtic_guardian():
    return MonsterCard.named(name='Celtic Guardian',
                             type='Normal',
                             race='Warrior',
                             attribute='Earth',
                             level=4,
                             attack=1400,
                             defense=1200,
                             description='An elf who learned to wield a sword, '
                                         'he baffles enemies with lightning-swift attacks.',
                             image=card_image())


def assert_monster_card_was_updated(monster_card, updated_monster_card, managed_monster_card):
    assert managed_monster_card == monster_card
    assert managed_monster_card.name == updated_monster_card.name
    assert managed_monster_card.race == updated_monster_card.race
    assert managed_monster_card.attribute == updated_monster_card.attribute
    assert managed_monster_card.level == updated_monster_card.level
    assert managed_monster_card.attack == updated_monster_card.attack
    assert managed_monster_card.defense == updated_monster_card.defense
    assert managed_monster_card.description == updated_monster_card.description
    if updated_monster_card.image.name == 'cards/card-back.jpg':
        assert managed_monster_card.image != updated_monster_card.image
    else:
        assert managed_monster_card.image == updated_monster_card.image


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
        assert exception_info.message_text() == 'There is already a card named Dark Magician.'
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

    def test_monster_card_image_is_not_updated(self):
        monster_card = dark_magician()
        updated_monster_card = MonsterCard.without_image_named(name='Celtic Guardian',
                                                               type='Normal',
                                                               race='Warrior',
                                                               attribute='Earth',
                                                               level=4,
                                                               attack=1400,
                                                               defense=1200,
                                                               description='An elf who learned to wield a sword, '
                                                                           'he baffles enemies with lightning-swift '
                                                                           'attacks.')
        self.system.store_monster_card(monster_card)
        self.system.update_monster_card_with(monster_card, updated_monster_card)
        with_the_only_one_in(self.system.monster_cards(),
                             lambda managed_monster_card:
                             assert_monster_card_was_updated(monster_card, updated_monster_card, managed_monster_card))

    def test_cannot_update_monster_card_where_there_is_one_with_same_name(self):
        monster_card = dark_magician()
        another_monster_card = celtic_guardian()
        updated_monster_card = monster_card_named(monster_card.name)
        self.system.store_monster_card(monster_card)
        self.system.store_monster_card(another_monster_card)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.update_monster_card_with(another_monster_card, updated_monster_card)
        assert exception_info.message_text() == 'There is already a card named Dark Magician.'
        assert_collections_have_same_elements([monster_card, another_monster_card], self.system.monster_cards())

    def test_querying_monster_card_by_name_fails_when_card_not_found(self):
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.monster_card_named('Dark Magician', if_found=lambda: pytest.fail())
        assert exception_info.message_text() == 'There is no card named Dark Magician.'

    def test_querying_monster_card_by_name(self):
        monster_card = dark_magician()
        self.system.store_monster_card(monster_card)
        found_monster_card = self.system.monster_card_named(monster_card.name, if_none=lambda: pytest.fail())
        assert found_monster_card == monster_card

    def test_querying_monster_card_by_id(self):
        monster_card = dark_magician()
        self.system.store_monster_card(monster_card)
        found_trap_card = self.system.monster_card_numbered(monster_card.id)
        assert found_trap_card == monster_card
