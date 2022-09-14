from django.urls import path
from .views import login, profile, signup

urlpatterns = [
    path('login', login, name="login"),
    path('profile', profile, name="profile"),
    path('signup', signup, name="signup"),
]
