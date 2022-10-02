from django.core.exceptions import ObjectDoesNotExist

from YuGiOh.cards import SpellCard, TrapCard, MonsterCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound
from persistence import managed_object_filtered_by


def raise_expected_to_be_found(managed_object):
    raise DataInconsistencyFound(f'{managed_object} was expected to be found, but it was not.')


def raise_found_card_named(name):
    raise SystemRestrictionInfringed(f'There is already a card named {name}.')


def raise_not_found_card_named(name):
    raise SystemRestrictionInfringed(f'There is no card named {name}.')


def card_named(name, repository, if_found, if_none):
    try:
        card = repository.get(name=name)
        return card if if_found is None else if_found(card)
    except ObjectDoesNotExist:
        return raise_not_found_card_named(name) if if_none is None else if_none()


class CardManagementSystem:

    def __init__(self):
        self.spell_cards_repository = SpellCard.objects
        self.trap_cards_repository = TrapCard.objects
        self.monster_cards_repository = MonsterCard.objects

    """ All Cards """

    def card_named(self, name, if_found=None, if_none=None):
        return self.spell_card_named(name,
                                     if_found=if_found,
                                     if_none=lambda:
                                     self.trap_card_named(name,
                                                          if_found=if_found,
                                                          if_none=
                                                          lambda: self.monster_card_named(name,
                                                                                          if_found=if_found,
                                                                                          if_none=if_none)))

    def assert_there_is_no_card_named(self, name):
        self.card_named(name, if_found=lambda _: raise_found_card_named(name), if_none=lambda: None)

    """ Spell Cards """

    def spell_cards(self):
        return list(self.spell_cards_repository.all())

    def store_spell_card(self, spell_card):
        self.assert_there_is_no_card_named(spell_card.name)
        spell_card.save()

    def purge_spell_card(self, spell_card):
        self.spell_card_numbered(spell_card.id,
                                 if_found=lambda _: spell_card.delete(),
                                 if_none=lambda: raise_expected_to_be_found(spell_card))

    def update_spell_card_with(self, spell_card, updated_spell_card):
        if spell_card.name != updated_spell_card.name:
            self.assert_there_is_no_card_named(updated_spell_card.name)
        spell_card.synchronize_with(updated_spell_card)
        spell_card.save()

    def spell_card_filtered_by(self, query_filter, if_found=None, if_none=None):
        return managed_object_filtered_by(query_filter=query_filter,
                                          repository=self.spell_cards_repository,
                                          if_found=if_found,
                                          if_none=if_none)

    def spell_card_named(self, name, if_found=None, if_none=None):
        return card_named(name,
                          repository=self.spell_cards_repository,
                          if_found=if_found,
                          if_none=if_none)

    def spell_card_numbered(self, spell_card_id, if_found=None, if_none=None):
        return self.spell_card_filtered_by(query_filter={'id': spell_card_id}, if_found=if_found, if_none=if_none)

    """ Trap Cards """

    def trap_cards(self):
        return list(self.trap_cards_repository.all())

    def store_trap_card(self, trap_card):
        self.assert_there_is_no_card_named(trap_card.name)
        trap_card.save()

    def purge_trap_card(self, trap_card):
        self.trap_card_numbered(trap_card.id,
                                if_found=lambda _: trap_card.delete(),
                                if_none=lambda: raise_expected_to_be_found(trap_card))

    def update_trap_card_with(self, trap_card, updated_trap_card):
        if trap_card.name != updated_trap_card.name:
            self.assert_there_is_no_card_named(updated_trap_card.name)
        trap_card.synchronize_with(updated_trap_card)
        trap_card.save()

    def trap_card_filtered_by(self, query_filter, if_found=None, if_none=None):
        return managed_object_filtered_by(query_filter=query_filter,
                                          repository=self.trap_cards_repository,
                                          if_found=if_found,
                                          if_none=if_none)

    def trap_card_named(self, name, if_found=None, if_none=None):
        return card_named(name,
                          repository=self.trap_cards_repository,
                          if_found=if_found,
                          if_none=if_none)

    def trap_card_numbered(self, trap_card_id, if_found=None, if_none=None):
        return self.trap_card_filtered_by(query_filter={'id': trap_card_id}, if_found=if_found, if_none=if_none)

    """ Monster Cards """

    def monster_cards(self):
        return list(self.monster_cards_repository.all())

    def store_monster_card(self, monster_card):
        self.assert_there_is_no_card_named(monster_card.name)
        monster_card.save()

    def purge_monster_card(self, monster_card):
        self.monster_card_numbered(monster_card.id,
                                   if_found=lambda _: monster_card.delete(),
                                   if_none=lambda: raise_expected_to_be_found(monster_card))

    def update_monster_card_with(self, monster_card, updated_monster_card):
        if monster_card.name != updated_monster_card.name:
            self.assert_there_is_no_card_named(updated_monster_card.name)
        monster_card.synchronize_with(updated_monster_card)
        monster_card.save()

    def monster_card_filtered_by(self, query_filter, if_found=None, if_none=None):
        return managed_object_filtered_by(query_filter=query_filter,
                                          repository=self.monster_cards_repository,
                                          if_found=if_found,
                                          if_none=if_none)

    def monster_card_named(self, name, if_found=None, if_none=None):
        return card_named(name,
                          repository=self.monster_cards_repository,
                          if_found=if_found,
                          if_none=if_none)

    def monster_card_numbered(self, monster_card_id, if_found=None, if_none=None):
        return self.monster_card_filtered_by(query_filter={'id': monster_card_id}, if_found=if_found, if_none=if_none)
