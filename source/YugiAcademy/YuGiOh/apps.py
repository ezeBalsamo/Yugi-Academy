from django.apps import AppConfig


class YugiohConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'YuGiOh'
    card_system = None
    booster_pack_system = None

    def ready(self):
        from .cards import CardManagementSystem
        from .booster_packs import BoosterPackManagementSystem
        self.card_system = CardManagementSystem()
        self.booster_pack_system = BoosterPackManagementSystem()
