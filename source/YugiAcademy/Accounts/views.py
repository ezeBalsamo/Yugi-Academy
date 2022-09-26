from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, UpdatePasswordForm


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
        return render(request, "login.html", {"form": AuthenticationForm()})

    raise Exception(f'The {request.method} method was not expected')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
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


@login_required
def update_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Password has been successfully updated")
            # Django will automagically redirect to login
        else:
            messages.error(request, 'Password update has failed.')
            return redirect('profile')

    if request.method == 'GET':
        return render(request, "update_password.html", {"form": UpdatePasswordForm(request.user)})

    raise Exception(f'The {request.method} method was not expected')


@login_required
def profile(request):
    return render(request, "profile.html")
