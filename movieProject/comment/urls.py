from django.urls import path
from .views import panel,insertData
urlpatterns = [
    path('',panel,name='panel'),
    path('insertData',insertData,name="insertData")
]