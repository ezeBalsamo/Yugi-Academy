from django.apps import apps

app = apps.get_app_config('YuGiOh')


def card_system():
    return app.card_system


def booster_pack_system():
    return app.booster_pack_system
