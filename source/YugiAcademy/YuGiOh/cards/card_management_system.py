from YuGiOh.cards import SpellCard


class CardManagementSystem:
    
    def __init__(self):
        self.spell_cards_repository = SpellCard.objects
    
    def spell_cards(self):
        return list(self.spell_cards_repository.all())

    def store_spell_card(self, spell_card):
        spell_card.save()
