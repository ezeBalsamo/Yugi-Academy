from django.core.exceptions import ObjectDoesNotExist

from YuGiOh.booster_packs import BoosterPack
from assertions import SystemRestrictionInfringed


def raise_found_booster_pack_named(name):
    raise SystemRestrictionInfringed(f'There is already a {BoosterPack.type_description} named {name}.')


def raise_not_found_booster_pack_named(name):
    raise SystemRestrictionInfringed(f'There is no {BoosterPack.type_description} named {name}.')


class BoosterPackManagementSystem:

    def __init__(self):
        self.booster_packs_repository = BoosterPack.objects

    def assert_there_is_no_booster_pack_named(self, name):
        self.booster_pack_named(name,
                                if_found=lambda booster_pack: raise_found_booster_pack_named(booster_pack.name),
                                if_none=lambda: None)

    def booster_packs(self):
        return list(self.booster_packs_repository.all())

    def store_booster_pack(self, booster_pack):
        self.assert_there_is_no_booster_pack_named(booster_pack.name)
        booster_pack.save()

    def booster_pack_named(self, name, if_found, if_none):
        try:
            card = self.booster_packs_repository.get(name=name)
            return card if if_found is None else if_found(card)
        except ObjectDoesNotExist:
            raise_not_found_booster_pack_named(name) if if_none is None else if_none()
