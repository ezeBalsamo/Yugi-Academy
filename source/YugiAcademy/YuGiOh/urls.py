from django.urls import path
from .views import home, login, about, cards, register_spell_card, booster_packs, register_booster_pack

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('about', about, name="about"),
    path('cards', cards, name="cards"),
    path('cards/registration', register_spell_card, name="register_spell_card"),
    path('booster-packs', booster_packs, name="booster-packs"),
    path('booster-packs/registration', register_booster_pack, name="register_booster_pack"),
]

