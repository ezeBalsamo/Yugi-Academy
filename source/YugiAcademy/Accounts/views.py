from django.apps import apps
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import SignUpForm, UpdatePasswordForm, UserAndProfileForm
from .models import UserProfile

user_profile_system = apps.get_app_config('Accounts').user_profile_management_system


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


def update_user_with_data_from(user, form_data):
    user.first_name = form_data.get('first_name')
    user.last_name = form_data.get('last_name')
    user.email = form_data.get('email')
    user.save()


def store_or_update_profile_of(user, request):
    form = UserAndProfileForm(request.POST, request.FILES)
    if form.is_valid():
        form_data = form.cleaned_data
        update_user_with_data_from(user, form_data)
        new_user_profile = UserProfile.from_form(user, form_data)
        user_profile_system.user_profile_of(user,
                                            if_found=lambda found_profile:
                                            user_profile_system.update_user_profile(found_profile, new_user_profile),
                                            if_none=lambda: new_user_profile.save())
        messages.info(request, "Profile has been successfully updated")
    else:
        messages.error(request, 'Profile update has failed.')


def user_and_profile_form(user_profile):
    user = user_profile.user
    return UserAndProfileForm(initial={
        'username': user.get_username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'description': user_profile.description,
        'social_network_link': user_profile.social_network_link,
        'avatar': user_profile.avatar
    })


def user_and_profile_form_when_no_profile(user):
    return UserAndProfileForm(initial={
        'username': user.get_username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    })


def form_to_show_profile_of(user, request):
    return user_profile_system.user_profile_of(user,
                                               if_found=lambda found_profile: user_and_profile_form(found_profile),
                                               if_none=lambda: user_and_profile_form_when_no_profile(user))


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        store_or_update_profile_of(user, request)
        return redirect('profile')
    elif request.method == 'GET':
        form = form_to_show_profile_of(user, request)
        return render(request, "profile.html", {"form": form})
    else:
        raise Exception(f'The {request.method} method was not expected')
