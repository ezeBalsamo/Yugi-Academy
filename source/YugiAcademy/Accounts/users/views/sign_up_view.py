from django.contrib import messages
from django.shortcuts import redirect, render

from users.forms import SignUpForm


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