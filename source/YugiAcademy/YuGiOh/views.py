from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "YuGiOh/index.html")


def cards(request):
    return render(request, "YuGiOh/cards.html")


def decks(request):
    return render(request, "YuGiOh/decks.html")


def about(request):
    return render(request, "YuGiOh/about.html")


def login(request):
    return render(request, "YuGiOh/login.html")
