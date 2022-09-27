from YuGiOh.booster_packs import BoosterPack, BoosterPackCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound
from persistence import managed_object_filtered_by


def raise_expected_to_be_found(managed_object):
    raise DataInconsistencyFound(f'{managed_object} was expected to be found, but it was not.')


def raise_found_booster_pack_named(name):
    raise SystemRestrictionInfringed(f'There is already a {BoosterPack.type_description} named {name}.')


def raise_found_booster_pack_card_identified_by(identifier):
    raise SystemRestrictionInfringed(
        f'There is already a {BoosterPackCard.type_description} identified by {identifier}.')


class BoosterPackManagementSystem:

    def __init__(self):
        self.booster_packs_repository = BoosterPack.objects
        self.booster_pack_cards_repository = BoosterPackCard.objects

    """ Booster packs """

    def assert_there_is_no_booster_pack_named(self, name):
        self.booster_pack_named(name,
                                if_found=lambda booster_pack: raise_found_booster_pack_named(booster_pack.name),
                                if_none=lambda: None)

    def assert_it_has_no_cards(self, booster_pack):
        booster_pack_cards = self.booster_pack_cards_in(booster_pack)
        if booster_pack_cards:
            raise SystemRestrictionInfringed(f'{booster_pack} cannot be deleted since it has cards.')

    def booster_packs(self):
        return list(self.booster_packs_repository.all())

    def store_booster_pack(self, booster_pack):
        self.assert_there_is_no_booster_pack_named(booster_pack.name)
        booster_pack.save()

    def purge_booster_pack(self, booster_pack):
        self.assert_it_has_no_cards(booster_pack)
        self.booster_pack_named(booster_pack.name,
                                if_found=lambda _: booster_pack.delete(),
                                if_none=lambda: raise_expected_to_be_found(booster_pack))

    def update_booster_pack_with(self, booster_pack, updated_booster_pack):
        if booster_pack.name != updated_booster_pack.name:
            self.assert_there_is_no_booster_pack_named(updated_booster_pack.name)
        booster_pack.synchronize_with(updated_booster_pack)
        booster_pack.save()

    def booster_pack_filtered_by(self, query_filter, if_found=None, if_none=None):
        return managed_object_filtered_by(query_filter=query_filter,
                                          repository=self.booster_packs_repository,
                                          if_found=if_found,
                                          if_none=if_none)

    def booster_pack_named(self, name, if_found=None, if_none=None):
        return self.booster_pack_filtered_by(query_filter={'name': name}, if_found=if_found, if_none=if_none)

    def booster_pack_numbered(self, booster_pack_id):
        return self.booster_pack_filtered_by(query_filter={'id': booster_pack_id})

    def booster_packs_named_like(self, partial_name):
        return self.booster_packs_repository.filter(name__icontains=partial_name)

    """ Booster pack cards """

    def assert_there_is_no_booster_pack_card_identified_by(self, identifier):
        self.booster_pack_card_identified_by(identifier,
                                             if_found=lambda booster_pack_card:
                                             raise_found_booster_pack_card_identified_by(booster_pack_card.identifier),
                                             if_none=lambda: None)

    def booster_pack_cards(self):
        return list(self.booster_pack_cards_repository.all())

    def store_booster_pack_card(self, booster_pack_card):
        self.assert_there_is_no_booster_pack_card_identified_by(booster_pack_card.identifier)
        booster_pack_card.save()

    def purge_booster_pack_card(self, booster_pack_card):
        self.booster_pack_card_identified_by(identifier=booster_pack_card.identifier,
                                             if_found=lambda _: booster_pack_card.delete(),
                                             if_none=lambda: raise_expected_to_be_found(booster_pack_card))

    def update_booster_pack_card_with(self, booster_pack_card, updated_booster_pack_card):
        if booster_pack_card.identifier != updated_booster_pack_card.identifier:
            self.assert_there_is_no_booster_pack_card_identified_by(updated_booster_pack_card.identifier)
        booster_pack_card.synchronize_with(updated_booster_pack_card)
        booster_pack_card.save()

    def booster_pack_card_filtered_by(self, query_filter, if_found=None, if_none=None):
        return managed_object_filtered_by(query_filter=query_filter,
                                          repository=self.booster_pack_cards_repository,
                                          if_found=if_found,
                                          if_none=if_none)

    def booster_pack_card_identified_by(self, identifier, if_found=None, if_none=None):
        return self.booster_pack_card_filtered_by({'identifier': identifier}, if_found=if_found, if_none=if_none)

    def booster_pack_cards_in(self, booster_pack):
        return self.booster_pack_cards_repository.filter(booster_pack=booster_pack)

    def booster_pack_card_numbered(self, booster_pack_card_id):
        return self.booster_pack_card_filtered_by({'id': booster_pack_card_id})
