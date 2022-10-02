from YuGiOh.cards.urls import urlpatterns as card_urls
from YuGiOh.booster_packs.urls import urlpatterns as booster_packs_urls

urlpatterns = card_urls + booster_packs_urls
