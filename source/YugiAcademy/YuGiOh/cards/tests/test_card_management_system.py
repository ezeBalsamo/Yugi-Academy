import collections

import pytest

from YuGiOh.cards import CardManagementSystem, SpellCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound


def pot_of_greed():
    return SpellCard.named(name='Pot of Greed', type='Normal', description='Draw 2 cards.')


def sogen():
    return SpellCard.named(name="Sogen",
                           type="Field",
                           description="All Warrior and Beast-Warrior monsters on the field gain 200 ATK/DEF.")


def with_the_only_one_in(collection, closure):
    assert len(collection) == 1
    closure(collection[0])


def assert_the_only_one_in(collection, expected_element):
    def assert_equals(element, another_element):
        assert element == another_element

    with_the_only_one_in(collection, lambda found_element: assert_equals(found_element, expected_element))


def assert_is_empty(collection):
    assert not collection


def assert_collections_have_same_elements(collection, another_collection):
    assert collections.Counter(collection) == collections.Counter(another_collection)


def assert_spell_card_was_updated(spell_card, updated_spell_card, managed_spell_card):
    assert managed_spell_card == spell_card
    assert managed_spell_card.name == updated_spell_card.name
    assert managed_spell_card.type == updated_spell_card.type
    assert managed_spell_card.description == updated_spell_card.description


@pytest.mark.django_db
def test_store_spell_card():
    system = CardManagementSystem()
    assert_is_empty(system.spell_cards())
    spell_card = pot_of_greed()
    system.store_spell_card(spell_card)
    assert_the_only_one_in(system.spell_cards(), spell_card)


@pytest.mark.django_db
def test_cannot_store_spell_card_when_there_is_one_with_same_name():
    system = CardManagementSystem()
    spell_card = pot_of_greed()
    another_spell_card = SpellCard.named(name=spell_card.name, type='Continuous', description='Win the game')
    system.store_spell_card(spell_card)
    with pytest.raises(SystemRestrictionInfringed) as exception_info:
        system.store_spell_card(another_spell_card)
    assert exception_info.message_text() == 'There is already a spell card named Pot of Greed.'
    assert_the_only_one_in(system.spell_cards(), spell_card)


@pytest.mark.django_db
def test_purge_spell_card():
    system = CardManagementSystem()
    spell_card = pot_of_greed()
    system.store_spell_card(spell_card)
    assert_the_only_one_in(system.spell_cards(), spell_card)
    system.purge_spell_card(spell_card)
    assert_is_empty(system.spell_cards())


@pytest.mark.django_db
def test_cannot_purge_spell_card_not_found():
    system = CardManagementSystem()
    spell_card = pot_of_greed()
    system.store_spell_card(spell_card)
    system.purge_spell_card(spell_card)
    with pytest.raises(DataInconsistencyFound) as exception_info:
        system.purge_spell_card(spell_card)
    assert exception_info.message_text() == 'Pot of Greed was expected to be found, but it was not.'
    assert_is_empty(system.spell_cards())


@pytest.mark.django_db
def test_update_spell_card():
    system = CardManagementSystem()
    spell_card = pot_of_greed()
    updated_spell_card = sogen()
    system.store_spell_card(spell_card)
    system.update_spell_card_with(spell_card, updated_spell_card)
    with_the_only_one_in(system.spell_cards(),
                         lambda managed_spell_card: assert_spell_card_was_updated(spell_card, updated_spell_card,
                                                                                  managed_spell_card))


@pytest.mark.django_db
def test_cannot_update_spell_card_where_there_is_one_with_same_name():
    system = CardManagementSystem()
    spell_card = pot_of_greed()
    another_spell_card = sogen()
    updated_spell_card = SpellCard.named(spell_card.name, type='Continuous', description='Win the game')
    system.store_spell_card(spell_card)
    system.store_spell_card(another_spell_card)
    with pytest.raises(SystemRestrictionInfringed) as exception_info:
        system.update_spell_card_with(another_spell_card, updated_spell_card)
    assert exception_info.message_text() == 'There is already a spell card named Pot of Greed.'
    assert_collections_have_same_elements([spell_card, another_spell_card], system.spell_cards())


@pytest.mark.django_db
def test_querying_spell_card_by_name_fails_when_card_not_found():
    system = CardManagementSystem()
    system.spell_card_named(name='Pot of Greed', if_found=lambda: pytest.fail(), if_none=lambda: None)


@pytest.mark.django_db
def test_querying_spell_card_by_name():
    system = CardManagementSystem()
    spell_card = pot_of_greed()
    system.store_spell_card(spell_card)
    found_spell_card = system.spell_card_named(name=spell_card.name, if_none=lambda: pytest.fail())
    assert found_spell_card == spell_card
