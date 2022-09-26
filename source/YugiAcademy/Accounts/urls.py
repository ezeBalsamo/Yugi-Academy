from django.urls import path

from .views import login_with

urlpatterns = [
    path('login', login_with, name="login"),
]
