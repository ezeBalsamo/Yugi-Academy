import pytest
from django.db.models.fields.files import ImageFieldFile, FileField

from YuGiOh.cards import CardManagementSystem, TrapCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound, \
    assert_is_empty, assert_the_only_one_in, \
    with_the_only_one_in, \
    assert_collections_have_same_elements


def card_image():
    return ImageFieldFile(instance=None, field=FileField(), name='cards/spell_cards/victory.jpg')


def jar_of_greed():
    return TrapCard.named(name='Jar of Greed', type='Normal', description='Draw 1 card.', image=card_image())


def magic_hammer():
    return TrapCard.named(name='Magic Hammer',
                          type='Counter',
                          description='When a Spell Card is activated: Discard'
                                      ' 1 card; negate the activation, and if'
                                      ' you do, destroy it.',
                          image=card_image())


def assert_trap_card_was_updated(trap_card, updated_trap_card, managed_trap_card):
    assert managed_trap_card == trap_card
    assert managed_trap_card.name == updated_trap_card.name
    assert managed_trap_card.type == updated_trap_card.type
    assert managed_trap_card.description == updated_trap_card.description
    if updated_trap_card.image.name == 'cards/card-back.jpg':
        assert managed_trap_card.image != updated_trap_card.image
    else:
        assert managed_trap_card.image == updated_trap_card.image


@pytest.mark.django_db
class TestCardManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.system = CardManagementSystem()

    def test_store_trap_card(self):
        assert_is_empty(self.system.trap_cards())
        trap_card = jar_of_greed()
        self.system.store_trap_card(trap_card)
        assert_the_only_one_in(self.system.trap_cards(), trap_card)

    def test_cannot_store_trap_card_when_there_is_one_with_same_name(self):
        trap_card = jar_of_greed()
        another_trap_card = TrapCard.named(name=trap_card.name,
                                           type='Continuous',
                                           description='Win the game',
                                           image=card_image())
        self.system.store_trap_card(trap_card)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.store_trap_card(another_trap_card)
        assert exception_info.message_text() == 'There is already a trap card named Jar of Greed.'
        assert_the_only_one_in(self.system.trap_cards(), trap_card)

    def test_purge_trap_card(self):
        trap_card = jar_of_greed()
        self.system.store_trap_card(trap_card)
        assert_the_only_one_in(self.system.trap_cards(), trap_card)
        self.system.purge_trap_card(trap_card)
        assert_is_empty(self.system.trap_cards())

    def test_cannot_purge_trap_card_not_found(self):
        trap_card = jar_of_greed()
        self.system.store_trap_card(trap_card)
        self.system.purge_trap_card(trap_card)
        with pytest.raises(DataInconsistencyFound) as exception_info:
            self.system.purge_trap_card(trap_card)
        assert exception_info.message_text() == 'Jar of Greed was expected to be found, but it was not.'
        assert_is_empty(self.system.trap_cards())

    def test_update_trap_card(self):
        trap_card = jar_of_greed()
        updated_trap_card = magic_hammer()
        self.system.store_trap_card(trap_card)
        self.system.update_trap_card_with(trap_card, updated_trap_card)
        with_the_only_one_in(self.system.trap_cards(),
                             lambda managed_trap_card: assert_trap_card_was_updated(trap_card, updated_trap_card,
                                                                                    managed_trap_card))

    def test_trap_card_image_is_not_updated(self):
        trap_card = jar_of_greed()
        updated_trap_card = TrapCard.without_image_named(name='Image',
                                                         type='Normal',
                                                         description="I don't have image")
        self.system.store_trap_card(trap_card)
        self.system.update_trap_card_with(trap_card, updated_trap_card)
        with_the_only_one_in(self.system.trap_cards(),
                             lambda managed_trap_card: assert_trap_card_was_updated(trap_card, updated_trap_card,
                                                                                    managed_trap_card))

    def test_cannot_update_trap_card_where_there_is_one_with_same_name(self):
        trap_card = jar_of_greed()
        another_trap_card = magic_hammer()
        updated_trap_card = TrapCard.named(trap_card.name,
                                           type='Continuous',
                                           description='Win the game',
                                           image=card_image())
        self.system.store_trap_card(trap_card)
        self.system.store_trap_card(another_trap_card)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.update_trap_card_with(another_trap_card, updated_trap_card)
        assert exception_info.message_text() == 'There is already a trap card named Jar of Greed.'
        assert_collections_have_same_elements([trap_card, another_trap_card], self.system.trap_cards())

    def test_querying_trap_card_by_name_fails_when_card_not_found(self):
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.trap_card_named('Jar of Greed', if_found=lambda: pytest.fail())
        assert exception_info.message_text() == 'There is no trap card named Jar of Greed.'

    def test_querying_trap_card_by_name(self):
        trap_card = jar_of_greed()
        self.system.store_trap_card(trap_card)
        found_trap_card = self.system.trap_card_named(trap_card.name, if_none=lambda: pytest.fail())
        assert found_trap_card == trap_card

    def test_querying_trap_card_by_id(self):
        trap_card = jar_of_greed()
        self.system.store_trap_card(trap_card)
        found_trap_card = self.system.trap_card_numbered(trap_card.id)
        assert found_trap_card == trap_card
