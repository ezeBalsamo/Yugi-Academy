from YuGiOh.website.urls import urlpatterns as website_urls
from YuGiOh.cards.urls import urlpatterns as card_urls
from YuGiOh.booster_packs.urls import urlpatterns as booster_packs_urls

urlpatterns = website_urls + card_urls + booster_packs_urls
