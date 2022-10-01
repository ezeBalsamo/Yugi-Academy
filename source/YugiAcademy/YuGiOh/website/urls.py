from django.urls import path

from YuGiOh.website.views import index, home, about

urlpatterns = [
    path('', index, name="index"),
    path('home', home, name="home"),
    path('about', about, name="about")
]
