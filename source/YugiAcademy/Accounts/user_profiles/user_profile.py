from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    type_description = 'user profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    social_network_link = models.URLField(null=True)
    avatar = models.ImageField(upload_to='avatars', null=True)

    @classmethod
    def from_form(cls, user, form_data):
        description = form_data.get('description')
        social_network_link = form_data.get('social_network_link')
        avatar = form_data.get('avatar')

        return cls(user=user, description=description, social_network_link=social_network_link, avatar=avatar)

    def username(self):
        return self.user.get_username()

    def __str__(self):
        return f'Profile of {self.username()}'

    def synchronize_with(self, user_profile):
        self.user = user_profile.user
        self.description = user_profile.description
        self.social_network_link = user_profile.social_network_link
        self.avatar = user_profile.avatar
