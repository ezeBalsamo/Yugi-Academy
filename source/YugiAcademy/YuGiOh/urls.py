from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('cards', views.cards, name="Cards"),
    path('decks', views.decks, name="Decks"),
    path('about', views.about, name="About"),
    path('login', views.login, name="Login"),
]
