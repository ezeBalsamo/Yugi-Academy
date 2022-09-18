from YuGiOh.cards import SpellCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound


class CardManagementSystem:
    
    def __init__(self):
        self.spell_cards_repository = SpellCard.objects
    
    def spell_cards(self):
        return list(self.spell_cards_repository.all())

    def store_spell_card(self, spell_card):
        if self.spell_cards_repository.filter(name=spell_card.name):
            raise SystemRestrictionInfringed(f'There is already a spell card named {spell_card.name}.')
        spell_card.save()

    def purge_spell_card(self, spell_card):
        if not self.spell_cards_repository.filter(name=spell_card.name):
            raise DataInconsistencyFound(f'{spell_card} was expected to be found, but it was not.')
        spell_card.delete()
