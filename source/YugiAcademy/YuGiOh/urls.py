from django.urls import path
from YuGiOh import views

urlpatterns = [
    path('', views.inicio),
    path('cards', views.cards)
]
