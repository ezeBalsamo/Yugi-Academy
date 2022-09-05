from django.urls import path
from .views import home, register_spell_card, cards, about, login

urlpatterns = [
    path('', home, name="home"),
    path('cards/registration', register_spell_card, name="register_spell_card"),
    path('cards', cards, name="cards"),
    path('about', about, name="about"),
    path('login', login, name="login"),
]
