from YuGiOh.booster_packs import BoosterPack


class BoosterPackManagementSystem:

    def __init__(self):
        self.booster_packs_repository = BoosterPack.objects

    def booster_packs(self):
        return list(self.booster_packs_repository.all())

    def store_booster_pack(self, booster_pack):
        booster_pack.save()
