from django.contrib import admin

from .models import MonsterCard, SpellCard, TrapCard, BoosterPack, BoosterPackCard

admin.site.register(MonsterCard)
admin.site.register(SpellCard)
admin.site.register(TrapCard)
admin.site.register(BoosterPack)
admin.site.register(BoosterPackCard)

