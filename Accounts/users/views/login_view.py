from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_with(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    if request.method == 'GET':
        return render(request, "login.html", {"form": AuthenticationForm()})

    raise Exception(f'The {request.method} method was not expected')
