from django.contrib.auth.models import User

from Accounts.user_profiles import UserProfile


def test_instance_creation_and_accessing():
    user = User(username='tom', password='tom the cat')
    form_data = {
        'description': 'I am tom',
        'social_network_link': 'https://www.facebook.com/tom',
        'avatar': 'tom.jpg'
    }
    user_profile = UserProfile.from_form(user=user, form_data=form_data)
    assert user_profile.description == 'I am tom'
    assert user_profile.social_network_link == 'https://www.facebook.com/tom'
    assert user_profile.avatar == 'tom.jpg'
    assert str(user_profile) == 'Profile of tom'
