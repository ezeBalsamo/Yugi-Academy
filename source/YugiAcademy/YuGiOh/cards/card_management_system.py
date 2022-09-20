from django.core.exceptions import ObjectDoesNotExist

from YuGiOh.cards import SpellCard, TrapCard, MonsterCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound


def raise_expected_to_be_found(managed_object):
    raise DataInconsistencyFound(f'{managed_object} was expected to be found, but it was not.')


def raise_found_card_named(name, card_type):
    raise SystemRestrictionInfringed(f'There is already a {card_type} named {name}.')


def raise_not_found_card_named(name, card_type):
    raise SystemRestrictionInfringed(f'There is no {card_type} named {name}.')


def card_named(name, card_type, repository, if_found, if_none):
    try:
        card = repository.get(name=name)
        return card if if_found is None else if_found(card)
    except ObjectDoesNotExist:
        raise_not_found_card_named(name, card_type) if if_none is None else if_none()


class CardManagementSystem:

    def __init__(self):
        self.spell_cards_repository = SpellCard.objects
        self.trap_cards_repository = TrapCard.objects
        self.monster_cards_repository = MonsterCard.objects

    """ Spell Cards """

    def assert_there_is_no_spell_card_named(self, name):
        self.spell_card_named(name=name,
                              if_found=lambda spell_card: raise_found_card_named(spell_card.name,
                                                                                 SpellCard.type_description),
                              if_none=lambda: None)

    def spell_cards(self):
        return list(self.spell_cards_repository.all())

    def store_spell_card(self, spell_card):
        self.assert_there_is_no_spell_card_named(spell_card.name)
        spell_card.save()

    def purge_spell_card(self, spell_card):
        self.spell_card_named(name=spell_card.name,
                              if_found=lambda _: spell_card.delete(),
                              if_none=lambda: raise_expected_to_be_found(spell_card))

    def update_spell_card_with(self, spell_card, updated_spell_card):
        if spell_card.name != updated_spell_card.name:
            self.assert_there_is_no_spell_card_named(updated_spell_card.name)
        spell_card.synchronize_with(updated_spell_card)
        spell_card.save()

    def spell_card_named(self, name, if_found=None, if_none=None):
        return card_named(name=name,
                          card_type=SpellCard.type_description,
                          repository=self.spell_cards_repository,
                          if_found=if_found,
                          if_none=if_none)

    """ Trap Cards """

    def assert_there_is_no_trap_card_named(self, name):
        self.trap_card_named(name=name,
                             if_found=lambda trap_card: raise_found_card_named(trap_card.name,
                                                                               TrapCard.type_description),
                             if_none=lambda: None)

    def trap_cards(self):
        return list(self.trap_cards_repository.all())

    def store_trap_card(self, trap_card):
        self.assert_there_is_no_trap_card_named(trap_card.name)
        trap_card.save()

    def purge_trap_card(self, trap_card):
        self.trap_card_named(name=trap_card.name,
                             if_found=lambda _: trap_card.delete(),
                             if_none=lambda: raise_expected_to_be_found(trap_card))

    def update_trap_card_with(self, trap_card, updated_trap_card):
        if trap_card.name != updated_trap_card.name:
            self.assert_there_is_no_trap_card_named(updated_trap_card.name)
        trap_card.synchronize_with(updated_trap_card)
        trap_card.save()

    def trap_card_named(self, name, if_found=None, if_none=None):
        return card_named(name=name,
                          card_type=TrapCard.type_description,
                          repository=self.trap_cards_repository,
                          if_found=if_found,
                          if_none=if_none)

    """ Monster Cards """

    def assert_there_is_no_monster_card_named(self, name):
        self.monster_card_named(name=name,
                                if_found=lambda monster_card: raise_found_card_named(monster_card.name,
                                                                                     MonsterCard.type_description),
                                if_none=lambda: None)

    def monster_cards(self):
        return list(self.monster_cards_repository.all())

    def store_monster_card(self, monster_card):
        self.assert_there_is_no_monster_card_named(monster_card.name)
        monster_card.save()

    def purge_monster_card(self, monster_card):
        self.monster_card_named(name=monster_card.name,
                                if_found=lambda _: monster_card.delete(),
                                if_none=lambda: raise_expected_to_be_found(monster_card))

    def update_monster_card_with(self, monster_card, updated_monster_card):
        if monster_card.name != updated_monster_card.name:
            self.assert_there_is_no_monster_card_named(updated_monster_card.name)
        monster_card.synchronize_with(updated_monster_card)
        monster_card.save()

    def monster_card_named(self, name, if_found=None, if_none=None):
        return card_named(name=name,
                          card_type=MonsterCard.type_description,
                          repository=self.monster_cards_repository,
                          if_found=if_found,
                          if_none=if_none)
