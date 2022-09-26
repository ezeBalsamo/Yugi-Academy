from django.contrib.auth.models import User

from Accounts.user_profiles import UserProfile


def test_instance_creation_and_accessing():
    user = User(username='tom', password='jerry')
    form_data = {
        'description': 'I am the super dev',
        'social_network_link': 'https://www.facebook.com',
        'avatar': 'spike.jpg'
    }
    user_profile = UserProfile.from_form(user=user, form_data=form_data)
    assert user_profile.description == 'I am the super dev'
    assert user_profile.social_network_link == 'https://www.facebook.com'
    assert user_profile.avatar == 'spike.jpg'
    assert str(user_profile) == 'Profile of tom'
