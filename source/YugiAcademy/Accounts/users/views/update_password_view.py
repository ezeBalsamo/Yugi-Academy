from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from Accounts.users.forms import UpdatePasswordForm


@login_required
def update_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Password has been successfully updated")
            return redirect('login')
        else:
            messages.error(request, 'Password update has failed.')
            return redirect('profile')

    if request.method == 'GET':
        return render(request, "update_password.html", {"form": UpdatePasswordForm(request.user)})

    raise Exception(f'The {request.method} method was not expected')
