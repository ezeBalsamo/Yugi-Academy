from django.urls import path

from .views import login_with, signup, profile

urlpatterns = [
    path('login', login_with, name="login"),
    path('signup', signup, name="signup"),
    path('profile', profile, name="profile"),
]
