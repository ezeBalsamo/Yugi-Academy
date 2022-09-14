from django.shortcuts import render, redirect
from .models import User
from .forms import SignUpForm, LogInForm, UserForm
from django.contrib import messages

user_log_in_page_context = {}


def user_log_in_page(user):
    global user_log_in_page_context

    user_log_in_page_context = {
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "name": user.name,
        "description": user.description,
        "web_site": user.web_site,
        "image": user.image
    }
    return user_log_in_page_context


def login(request):
    user_found = None
    display_message = 'Username does not exist'

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = \
                User(username=form_data.get('username'),
                     password=form_data.get('password'))

            try:
                user_found = User.objects.get(username=user.username)

            except:
                display_message = 'Username does not exist'

            if user_found is not None:
                if user.password == user_found.password:
                    user_context = user_log_in_page(user_found)
                    return render(request, 'YuGiOh/cards.html', user_context)

                else:
                    display_message = 'The password is wrong'
                    messages.info(request, display_message)
                    return redirect('login')

            else:
                messages.info(request, display_message)
                return redirect('login')

        else:
            display_message = 'Enter valid information'
            messages.info(request, display_message)
            return redirect('login')

    if request.method == 'GET':
        context = {
            'form': LogInForm(request.GET)
        }

        return render(request, 'login.html', context)


def signup(request):
    user_found_by_username = None
    email_found = None
    display_message = 'Username or email had already been used'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = \
                User(email=form_data.get('email'),
                     username=form_data.get('username'),
                     password=form_data.get('password'))

            try:
                user_found_by_username = User.objects.get(username=user.username)

            except:
                display_message = 'Username has already been used'

            try:
                email_found = User.objects.get(email=user.email)

            except:
                display_message = 'Email has already been used'

            if user_found_by_username is None and email_found is None:
                user.save()
                return redirect('YuGiOh/cards')

            else:
                messages.info(request, display_message)
                return redirect('signup')

        else:
            display_message = 'Enter valid information'
            messages.info(request, display_message)
            return redirect('signup')

    if request.method == 'GET':
        context = {
            'form': SignUpForm(request.GET)
        }

        return render(request, 'signup.html', context)


def profile(request):
    global user_log_in_page_context
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = \
                User(email=form_data.get('email'),
                     username=form_data.get('username'),
                     password=form_data.get('password'),
                     name=form_data.get('name'),
                     description=form_data.get('description'),
                     web_site=form_data.get('web_site'),
                     image=form_data.get('image'))

            user_found_by_username = User.objects.get(username=user.username)
            user_found_by_username.name = user.name
            user_found_by_username.description = user.description
            user_found_by_username.web_site = user.web_site
            user_found_by_username.image = user.image

            user_found_by_username.save()

            user_log_in_page_context['name'] = user_found_by_username.name
            user_log_in_page_context['description'] = user_found_by_username.description
            user_log_in_page_context['web_site'] = user_found_by_username.web_site
            user_log_in_page_context['image'] = user_found_by_username.image

            return render(request, "profile.html", user_log_in_page_context)

    return render(request, "profile.html", user_log_in_page_context)
