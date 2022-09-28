from django.urls import path

from Accounts.user_profiles.views import update_profile

urlpatterns = [
    path('profile', update_profile, name="profile")
]
