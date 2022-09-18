import pytest

from YuGiOh.cards import CardManagementSystem, SpellCard
from assertions import SystemRestrictionInfringed


def pot_of_greed():
    return SpellCard.named(name='Pot of Greed', type='Normal', description='Draw 2 cards.')


def assert_the_only_one_in(collection, element):
    assert len(collection) == 1
    assert collection[0] == element


def assert_is_empty(collection):
    assert not collection


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
    assert exception_info.message_text() == 'There is already a spell card named Pot of Greed'
    assert_the_only_one_in(system.spell_cards(), spell_card)


@pytest.mark.django_db
def test_purge_spell_card():
    system = CardManagementSystem()
    spell_card = pot_of_greed()
    system.store_spell_card(spell_card)
    assert_the_only_one_in(system.spell_cards(), spell_card)
    system.purge_spell_card(spell_card)
    assert_is_empty(system.spell_cards())
