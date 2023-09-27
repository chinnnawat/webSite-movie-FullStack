from django.urls import path
from .views import homePage, showPlayer

urlpatterns = [
    path('', homePage),
    path('player/<int:id>', showPlayer, name='player_detail'),
]
