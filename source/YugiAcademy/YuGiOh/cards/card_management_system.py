from YuGiOh.cards import SpellCard
from assertions import SystemRestrictionInfringed


class CardManagementSystem:
    
    def __init__(self):
        self.spell_cards_repository = SpellCard.objects
    
    def spell_cards(self):
        return list(self.spell_cards_repository.all())

    def store_spell_card(self, spell_card):
        if self.spell_cards_repository.filter(name=spell_card.name):
            raise SystemRestrictionInfringed(f'There is already a spell card named {spell_card.name}')
        spell_card.save()
