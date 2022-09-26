import pytest
from django.contrib.auth.models import User

from Accounts.user_profiles import UserProfileManagementSystem, UserProfile
from assertions import SystemRestrictionInfringed, \
                        assert_is_empty, assert_the_only_one_in, \
                        with_the_only_one_in, \
                        assert_collections_have_same_elements


def tom():
    return User(username='tom', password='tom_the_cat')


def jerry():
    return User(username='jerry', password='jerry_the_mouse')


def user_profile_for(user):
    username = user.get_username()
    form_data = {
        'description': f'I am {username}',
        'social_network_link': f'https://www.facebook.com/{username}',
        'avatar': f'{username}.jpg'
    }
    return UserProfile.from_form(user=user, form_data=form_data)


def tom_user_profile():
    user = tom()
    user.save()
    return user_profile_for(user)


def jerry_user_profile():
    user = jerry()
    user.save()
    return user_profile_for(user)


def assert_user_profile_was_updated(user_profile, updated_user_profile, managed_user_profile):
    assert managed_user_profile == user_profile
    assert managed_user_profile.description == updated_user_profile.description
    assert managed_user_profile.social_network_link == updated_user_profile.social_network_link
    assert managed_user_profile.avatar == updated_user_profile.avatar


@pytest.mark.django_db
class TestUserProfileManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.system = UserProfileManagementSystem()

    def test_store_spell_card(self):
        assert_is_empty(self.system.user_profiles())
        user_profile = tom_user_profile()
        self.system.store_user_profile(user_profile)
        assert_the_only_one_in(self.system.user_profiles(), user_profile)

    def test_cannot_store_spell_card_when_there_is_one_for_the_same_user(self):
        user_profile = tom_user_profile()
        another_user_profile = user_profile_for(user_profile.user)
        self.system.store_user_profile(user_profile)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.store_user_profile(another_user_profile)
        assert exception_info.message_text() == 'There is already a user profile for tom.'
        assert_the_only_one_in(self.system.user_profiles(), user_profile)

    def test_update_user_profile(self):
        user_profile = tom_user_profile()
        updated_user_profile = jerry_user_profile()
        self.system.store_user_profile(user_profile)
        self.system.update_user_profile_with(user_profile, updated_user_profile)
        with_the_only_one_in(self.system.user_profiles(),
                             lambda managed_user_profile:
                             assert_user_profile_was_updated(user_profile, updated_user_profile, managed_user_profile))

    def test_cannot_update_user_profile_where_there_is_one_for_the_same_user(self):
        user_profile = tom_user_profile()
        another_user_profile = jerry_user_profile()
        updated_user_profile = user_profile_for(user_profile.user)
        self.system.store_user_profile(user_profile)
        self.system.store_user_profile(another_user_profile)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.update_user_profile_with(another_user_profile, updated_user_profile)
        assert exception_info.message_text() == 'There is already a user profile for tom.'
        assert_collections_have_same_elements([user_profile, another_user_profile], self.system.user_profiles())

    def test_querying_user_profile_by_user_fails_when_user_not_found(self):
        user = tom()
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.user_profile_of(user, if_found=lambda: pytest.fail())
        assert exception_info.message_text() == 'There is no user profile of tom.'

    def test_querying_user_profile_by_user(self):
        user_profile = tom_user_profile()
        self.system.store_user_profile(user_profile)
        found_user_profile = self.system.user_profile_of(user_profile.user, if_none=lambda: pytest.fail())
        assert found_user_profile == user_profile
