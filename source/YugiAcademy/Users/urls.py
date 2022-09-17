from django.urls import path
from .views import login, profile, signup, change_password

urlpatterns = [
    path('login', login, name="login"),
    path('profile', profile, name="profile"),
    path('signup', signup, name="signup"),
    path('change-password', change_password, name="change_password"),
]
