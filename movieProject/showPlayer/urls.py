from django.urls import path
from showPlayer.views import  showPlayer,searchCategory

urlpatterns = [
    path('player/<int:id>', showPlayer, name='player_detail'),
    path('webblogs/category/<int:cat_id>',searchCategory,name='searchCategory')
]