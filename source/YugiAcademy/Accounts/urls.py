from Accounts.users.urls import urlpatterns as user_urls
from Accounts.user_profiles.urls import urlpatterns as user_profile_urls

urlpatterns = user_urls + user_profile_urls
