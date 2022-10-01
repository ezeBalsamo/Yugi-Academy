import pytest
from django.db.models.fields.files import ImageFieldFile, FileField

from YuGiOh.cards import CardManagementSystem, SpellCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound, \
    assert_is_empty, assert_the_only_one_in, \
    with_the_only_one_in, \
    assert_collections_have_same_elements


def card_image():
    return ImageFieldFile(instance=None, field=FileField(), name='cards/spell_cards/victory.jpg')


def pot_of_greed():
    return SpellCard.named(name='Pot of Greed',
                           type='Normal',
                           description='Draw 2 cards.',
                           image=card_image())


def sogen():
    return SpellCard.named(name="Sogen",
                           type="Field",
                           description="All Warrior and Beast-Warrior monsters on the field gain 200 ATK/DEF.",
                           image=card_image())


def assert_spell_card_was_updated(spell_card, updated_spell_card, managed_spell_card):
    assert managed_spell_card == spell_card
    assert managed_spell_card.name == updated_spell_card.name
    assert managed_spell_card.type == updated_spell_card.type
    assert managed_spell_card.description == updated_spell_card.description
    if updated_spell_card.image.name == 'cards/card-back.jpg':
        assert managed_spell_card.image != updated_spell_card.image
    else:
        assert managed_spell_card.image == updated_spell_card.image


@pytest.mark.django_db
class TestCardManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.system = CardManagementSystem()

    def test_store_spell_card(self):
        assert_is_empty(self.system.spell_cards())
        spell_card = pot_of_greed()
        self.system.store_spell_card(spell_card)
        assert_the_only_one_in(self.system.spell_cards(), spell_card)

    def test_cannot_store_spell_card_when_there_is_one_with_same_name(self):
        spell_card = pot_of_greed()
        another_spell_card = SpellCard.named(name=spell_card.name,
                                             type='Continuous',
                                             description='Win the game',
                                             image=card_image())
        self.system.store_spell_card(spell_card)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.store_spell_card(another_spell_card)
        assert exception_info.message_text() == 'There is already a spell card named Pot of Greed.'
        assert_the_only_one_in(self.system.spell_cards(), spell_card)

    def test_purge_spell_card(self):
        spell_card = pot_of_greed()
        self.system.store_spell_card(spell_card)
        assert_the_only_one_in(self.system.spell_cards(), spell_card)
        self.system.purge_spell_card(spell_card)
        assert_is_empty(self.system.spell_cards())

    def test_cannot_purge_spell_card_not_found(self):
        spell_card = pot_of_greed()
        self.system.store_spell_card(spell_card)
        self.system.purge_spell_card(spell_card)
        with pytest.raises(DataInconsistencyFound) as exception_info:
            self.system.purge_spell_card(spell_card)
        assert exception_info.message_text() == 'Pot of Greed was expected to be found, but it was not.'
        assert_is_empty(self.system.spell_cards())

    def test_update_spell_card(self):
        spell_card = pot_of_greed()
        updated_spell_card = sogen()
        self.system.store_spell_card(spell_card)
        self.system.update_spell_card_with(spell_card, updated_spell_card)
        with_the_only_one_in(self.system.spell_cards(),
                             lambda managed_spell_card: assert_spell_card_was_updated(spell_card, updated_spell_card,
                                                                                      managed_spell_card))

    def test_spell_card_image_is_not_updated(self):
        spell_card = pot_of_greed()
        updated_spell_card = SpellCard.without_image_named(name='Image',
                                                           type='Normal',
                                                           description="I don't have image")
        self.system.store_spell_card(spell_card)
        self.system.update_spell_card_with(spell_card, updated_spell_card)
        with_the_only_one_in(self.system.spell_cards(),
                             lambda managed_spell_card: assert_spell_card_was_updated(spell_card, updated_spell_card,
                                                                                      managed_spell_card))

    def test_cannot_update_spell_card_where_there_is_one_with_same_name(self):
        spell_card = pot_of_greed()
        another_spell_card = sogen()
        updated_spell_card = SpellCard.named(spell_card.name,
                                             type='Continuous',
                                             description='Win the game',
                                             image=card_image())
        self.system.store_spell_card(spell_card)
        self.system.store_spell_card(another_spell_card)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.update_spell_card_with(another_spell_card, updated_spell_card)
        assert exception_info.message_text() == 'There is already a spell card named Pot of Greed.'
        assert_collections_have_same_elements([spell_card, another_spell_card], self.system.spell_cards())

    def test_querying_spell_card_by_name_fails_when_card_not_found(self):
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.spell_card_named('Pot of Greed', if_found=lambda: pytest.fail())
        assert exception_info.message_text() == 'There is no spell card named Pot of Greed.'

    def test_querying_spell_card_by_name(self):
        spell_card = pot_of_greed()
        self.system.store_spell_card(spell_card)
        found_spell_card = self.system.spell_card_named(spell_card.name, if_none=lambda: pytest.fail())
        assert found_spell_card == spell_card

    def test_querying_spell_card_by_id(self):
        spell_card = pot_of_greed()
        self.system.store_spell_card(spell_card)
        found_spell_card = self.system.spell_card_numbered(spell_card.id)
        assert found_spell_card == spell_card
