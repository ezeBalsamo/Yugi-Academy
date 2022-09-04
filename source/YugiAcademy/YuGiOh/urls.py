from django.urls import path
from YuGiOh import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cards', views.cards, name="Cards"),
    path('decks', views.decks, name="Decks")
]
