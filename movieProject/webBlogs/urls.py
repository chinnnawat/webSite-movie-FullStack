from django.urls import path
from .views import homePage
urlpatterns = [
    path('', homePage,name="homePage"),
    # path('player/<int:id>', showPlayer, name='player_detail'),
    # path('webblogs/category/<int:cat_id>',searchCategory,name='searchCategory')
]
