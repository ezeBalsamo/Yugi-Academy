from django.core.exceptions import ObjectDoesNotExist

from YuGiOh.cards import SpellCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound


def raise_not_found_spell_card_named(name):
    raise SystemRestrictionInfringed(f'There is no spell card named {name}.')


def raise_found_spell_card_named(name):
    raise SystemRestrictionInfringed(f'There is already a spell card named {name}.')


class CardManagementSystem:

    def __init__(self):
        self.spell_cards_repository = SpellCard.objects

    def assert_there_is_no_spell_card_named(self, name):
        self.spell_card_named(name=name,
                              if_found=lambda spell_card: raise_found_spell_card_named(spell_card.name),
                              if_none=lambda: None)

    def spell_cards(self):
        return list(self.spell_cards_repository.all())

    def store_spell_card(self, spell_card):
        self.assert_there_is_no_spell_card_named(spell_card)
        spell_card.save()

    def purge_spell_card(self, spell_card):
        if not self.spell_cards_repository.filter(name=spell_card.name):
            raise DataInconsistencyFound(f'{spell_card} was expected to be found, but it was not.')
        spell_card.delete()

    def update_spell_card_with(self, spell_card, updated_spell_card):
        if spell_card.name != updated_spell_card.name:
            self.assert_there_is_no_spell_card_named(updated_spell_card.name)
        spell_card.synchronize_with(updated_spell_card)
        spell_card.save()

    def spell_card_named(self, name, if_found=None, if_none=None):

        try:
            spell_card = self.spell_cards_repository.get(name=name)
            return spell_card if if_found is None else if_found(spell_card)
        except ObjectDoesNotExist:
            raise_not_found_spell_card_named(name) if if_none is None else if_none()
