from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from YuGiOh.booster_packs.forms import SearchBoosterPackForm
from YuGiOh.models import app


def booster_packs_according_to(request):
    if request.method == 'POST':
        form = SearchBoosterPackForm(request.POST)
        if form.is_valid():
            partial_name = form.cleaned_data.get('name')
            return app.booster_pack_system.booster_packs_named_like(partial_name)
        else:
            raise Exception(f'The {form} is not valid.')

    if request.method == 'GET':
        return list()

    raise Exception(f'The {request.method} method was not expected')


@login_required
def booster_packs(request):
    context = {
        'form': SearchBoosterPackForm(),
        'booster_packs': booster_packs_according_to(request)
    }
    return render(request, "YuGiOh/booster_packs.html", context)
