from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import login_with, signup, update_password, profile

urlpatterns = [
    path('login', login_with, name="login"),
    path('signup', signup, name="signup"),
    path('logout', LogoutView.as_view(template_name='index.html'), name="logout"),
    path('update-password', update_password, name="update_password"),
    path('profile', profile, name="profile"),
]
