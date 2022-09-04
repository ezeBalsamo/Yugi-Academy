from django.shortcuts import render


# Create your views here.

def inicio(request):
    return render(request, "YuGiOh/index2.html")


def cards(request):
    return render(request, "YuGiOh/cards.html")

def decks(request):
    return render(request, "YuGiOh/decks.html")
