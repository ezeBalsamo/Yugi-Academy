import pytest

from YuGiOh.cards import CardManagementSystem, SpellCard


def pot_of_greed():
    return SpellCard.named(name='Pot of Greed', type='Normal', description='Draw 2 cards.')


def assert_the_only_one_in(collection, element):
    assert len(collection) == 1
    assert collection[0] == element


def assert_is_empty(collection):
    assert not collection


@pytest.mark.django_db
def test_register_spell_card():
    system = CardManagementSystem()
    assert_is_empty(system.spell_cards())
    spell_card = pot_of_greed()
    system.store_spell_card(spell_card)
    assert_the_only_one_in(system.spell_cards(), spell_card)
