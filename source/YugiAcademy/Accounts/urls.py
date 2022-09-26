from django.urls import path

from .views import login_with, signup

urlpatterns = [
    path('login', login_with, name="login"),
    path('signup', signup, name="signup"),
]
