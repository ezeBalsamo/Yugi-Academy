from django.core.exceptions import ObjectDoesNotExist

from Accounts.user_profiles import UserProfile
from assertions import SystemRestrictionInfringed


def raise_found_user_profile_of(user):
    raise SystemRestrictionInfringed(f'There is already a {UserProfile.type_description} for {user.get_username()}.')


def raise_not_found_user_profile_of(user):
    raise SystemRestrictionInfringed(f'There is no {UserProfile.type_description} of {user.get_username()}.')


class UserProfileManagementSystem:

    def __init__(self):
        self.user_profiles_repository = UserProfile.objects

    def assert_there_is_no_user_profile_for(self, user):
        self.user_profile_of(user,
                             if_found=lambda user_profile: raise_found_user_profile_of(user_profile.user),
                             if_none=lambda: None)

    def user_profiles(self):
        return list(self.user_profiles_repository.all())

    def store_user_profile(self, user_profile):
        self.assert_there_is_no_user_profile_for(user_profile.user)
        user_profile.save()

    def update_user_profile_with(self, user_profile, updated_user_profile):
        if user_profile.user != updated_user_profile.user:
            self.assert_there_is_no_user_profile_for(updated_user_profile.user)
        user_profile.synchronize_with(updated_user_profile)
        user_profile.save()

    def user_profile_of(self, user, if_found=None, if_none=None):
        try:
            user_profile = self.user_profiles_repository.get(user=user)
            return user_profile if if_found is None else if_found(user_profile)
        except ObjectDoesNotExist:
            raise_not_found_user_profile_of(user) if if_none is None else if_none()
