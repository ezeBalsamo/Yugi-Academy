from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def about(request):
    return render(request, "about.html")
