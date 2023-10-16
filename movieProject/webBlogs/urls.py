from django.urls import path
from .views import homePage,search,submit_review
urlpatterns = [
    path('', homePage,name="homePage"),
    path('search',search,name="searchMovie"),
    path('submit_review/<int:id>/',submit_review,name="submit_review"),
]
