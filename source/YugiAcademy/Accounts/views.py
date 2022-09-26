from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm


def login_with(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return render(request, 'YuGiOh/cards.html')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    if request.method == 'GET':
        return render(request, "login.html")

    raise Exception(f'The {request.method} method was not expected')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Sign up has been successful")
            return redirect('login')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('signup')

    if request.method == 'GET':
        return render(request, "signup.html", {"form": SignUpForm()})

    raise Exception(f'The {request.method} method was not expected')
