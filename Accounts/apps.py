from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Accounts'
    user_profile_management_system = None

    def ready(self):
        from .user_profiles import UserProfileManagementSystem
        self.user_profile_management_system = UserProfileManagementSystem()
